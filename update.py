import requests, re, html, os, time, json
from enum import Enum

template_versions = { 'subsilver': 'phpBB2', 'prosilver': 'phpBB3', 'punbb': 'PunBB', 'invision': 'Invision' }
template_categories = { 'main':'Général', 'portal':'Portail', 'gallery':'Galerie', 'calendar':'Calendrier', 'group':'Groupes', 'post':'Poster & Messages Privés', 'moderation':'Modération', 'profil':'Profil'}
template_descriptions = { cat:{} for cat in template_categories }
template_contents = { ver:{} for ver in template_versions }
template_from_categories = {}

start_time = time.time()

script_dir = os.path.dirname(os.path.abspath(__file__))

os.makedirs(script_dir+'/var', exist_ok=True)
os.makedirs(script_dir+'/tpl', exist_ok=True)

for i in template_versions.keys():
    os.makedirs(script_dir+'/src/'+i, exist_ok=True)

num_page = 0
s = requests.Session()

from ident import ident
''' 
# file ident.py to add in current directory not included, with forum adress and admin identification, e.g :
ident = {'forum': 'http://forum.forumactif.com/', 'username':'Gizmo', 'password': 'What did you expect?'}
'''

f = ident['forum'] 

# connect to forum
tid = s.post(f+'login.forum', data={'username':ident['username'], 'password':ident['password'], 'login':1, 'redirect':'/admin/', 'admin':1}).url[49:]

limit = 500

i = limit


'''Chargement des pages du forum'''
for ver in template_versions:
    
    j = 300
    # change forum theme
    s.post(f+'admin/index.forum?part=themes&sub=styles&mode=version&extended_admin=1&tid='+tid,data={'tpl':ver, 'keep_theme': 1, 'change_version': 1})

    for cat in template_categories:
        k = 300

        cat_page = s.get(f+'admin/index.forum?mode='+cat+'&part=themes&sub=templates&tid='+tid)
        cat_page.encoding = 'utf-8'
        cat_page = cat_page.text

        result= re.findall('>([a-z0-9_]+)(?:</span>)?</a></strong></td><td class="row1" align="center" valign="middle"><i>([^<]+)</i></td><td class="row2" align="center" valign="middle" style="text-align:center;"><a href="/(admin/index\.forum\?[^"]+)"', cat_page)

        for tem, desc, url in result:
        
            template_descriptions[cat][tem] = desc
            template_from_categories[tem] = cat
            if os.path.isfile(script_dir+'/src/'+ver+'/'+tem+'.tpl'):
                with open(script_dir+'/src/'+ver+'/'+tem+'.tpl', 'r') as t:
                    template_contents[ver][tem] = t.read()
            else:
                time.sleep(2)
                tem_page = s.get(f+html.unescape(url))
                tem_page.encoding = 'utf-8'
                tem_page = tem_page.text

                # on prend le contenu
                num_page += 1
                print(str(num_page) +' : '+ ver+'|'+cat+'|'+tem+'|'+str(-start_time+time.time()))
                try:
                    template_contents[ver][tem] = html.unescape(re.search('<textarea [^>]+>([\s\S]*)</textarea>', tem_page).group(1))
                except Exception:
                    print(tem_page)
                    import sys
                    sys.exit()

                # ecriture dans fichier src/version/nom_template
                with open(script_dir+'/src/'+ver+'/'+tem+'.tpl', 'w') as t:
                    t.write(template_contents[ver][tem])

            k -= 1
            if k == 0:
                break
        j -= 1
        if j == 0:
            break
    i -= 1
    if i == 0:
        break

'''Fichier README.md'''
with open(script_dir+'/README.md', 'w') as f:
    f.write('# Templates de Forumactif\n\n## Variables\n\n* [Liste totale](variables.md#readme)\n\n\t* [Avec description](variables_avec_description.md#readme)\n\t* [Sans description](variables_sans_description.md#readme)\n\n## Templates\n\n')
    
    for cat in sorted(template_categories, key=template_categories.get): 

        f.write('### '+template_categories[cat]+'\n\n')

        for tem in sorted(template_descriptions[cat]):

            f.write('* __[`'+tem+'`](tpl/'+tem+'.md#readme) :__ '+template_descriptions[cat][tem]+'\n')

        f.write('\n')

variables = {}

all_desc = json.loads(requests.get('https://fa-tvars.appspot.com/export').text)
var_desc = all_desc[0]
templates_desc = all_desc[1]

template_variables = { tem:{} for tem in template_contents['subsilver'] }

'''Parsing des templates'''
for ver in template_contents:

    for tem in template_contents[ver]:

        template_lines = template_contents[ver][tem].split('\n')

        num_line = 0

        stack = ''

        for l in template_lines:

            num_line += 1
            matches = re.findall('(\{[A-Za-z._0-9-]+\}|<!-- (?:END|BEGIN) [A-Za-z._0-9-]+ -->)', l)

            for m in matches:

                if m[0] == '{':
                    var_name = m[1:-1]
                    var_type = 0
                elif m[5] == 'B':
                    if stack!='':   
                        stack += '.'
                    stack += m[11:-4]
                    var_name = stack
                    var_type = 1
                else:
                    var_name = stack
                    stack = '.'.join(stack.split('.')[:-1])
                    var_type = 2
                    
                if var_name not in variables:
                    variables[var_name] = {}
                if ver not in variables[var_name]:
                    variables[var_name][ver] = {}
                if tem  not in variables[var_name][ver]:
                    variables[var_name][ver][tem] = []

                if var_name not in template_variables[tem]:
                    template_variables[tem][var_name] = []
                    
                variables[var_name][ver][tem] += [[num_line, var_type]]
                template_variables[tem][var_name] += [[num_line, var_type, ver]]

def sorting_version(ver):
    return { 'subsilver': 1, 'prosilver': 0, 'punbb': 2, 'invision': 3 }[ver]

'''Write one file by variable'''
for var in variables:

    with open(script_dir+'/var/'+var+'.md', 'w') as f:

        f.write('# ' + var +'\n* __Type :__ ')

        types = [x[1] for v in variables[var].values() for u in v.values() for x in u]
        if '.' in var:
            f.write('sous-')
        f.write('variable d')
        if 0 in types:
            f.write('\'affichage')
            if 1 in types:
                f.write(' et d')
        if 1 in types:
            f.write('e bouclage')

        f.write('\n* __Utilisable dans :__ ')
        f.write(', '.join(['[`'+t+'`](../tpl/'+t+'.md#readme)' for t in sorted(set([key for ver in variables[var].values() for key in ver.keys()]))]))

        #set([u[4] for u in variables[var]]))]))
        f.write('\n* __Utilisation :__\n\n```html\n')

        # TODO afficher autres types
        f.write('{' + var + '}\n')

        f.write('```\n\n## Description[*](https://fa-tvars.appspot.com/var/'+var+')\n')
        # TODO load description or display add description
        if var not in var_desc:
            f.write('[*Ajouter une description*](https://fa-tvars.appspot.com/var/'+var+')')
        else:
            f.write(var_desc[var])

        f.write('\n\n## Utilisations dans les templates\n\n')

        for ver in sorted(variables[var].keys(), key=sorting_version):
            f.write('### Version '+template_versions[ver]+'\n')
            for tem in sorted(variables[var][ver].keys()):
                for num_line, var_type in variables[var][ver][tem]:
                    f.write('* __[`'+tem+'`](../tpl/'+tem+'.md#readme) :__ lignes [`'+str(num_line)+'`](../src/'+ver+'/'+tem+'.tpl#L'+str(num_line)+')[`<->`](../src/'+ver+'/'+tem+'.tpl#L'+str(num_line)+'-L'+str(num_line)+')[`'+str(num_line)+'`](../src/'+ver+'/'+tem+'.tpl#L'+str(num_line)+')\n')
            f.write('\n')


def var2text(var, vtype):
    if 0 == vtype:
        levels = var.split('.')
        return ((len(levels)-1)*'&nbsp;'*4)+'[`{'+var+'}`]'
    elif 1 == vtype:
        levels = var.split('.')
        return ((len(levels)-1)*'&nbsp;'*4)+'[`<!-- BEGIN '+levels[-1]+' -->`]'
    elif 2 == vtype:
        levels = var.split('.')
        return ((len(levels)-1)*'&nbsp;'*4)+'[`<!-- END '+levels[-1]+' -->`]'

def var2links(var, types):
    links = []
    for vtype in types:
        links += [var2text(var,vtype)+'(../var/'+var+'.md#readme)']
    return links

'''Write one file by template'''
for tem in template_variables:

    with open(script_dir+'/tpl/'+tem+'.md', 'w') as f:

        f.write('# Template ' + tem +'\n* [Chemin](#chemin)\n* [Description](#description)\n* [Variables disponibles](#variables-disponibles)\n* Template par défaut : [`phpBB3`](#template-par-dfaut-phpbb3) [`phpBB2`](#template-par-dfaut-phpbb2) [`PunBB`](#template-par-dfaut-punbb) [`Invision`](#template-par-dfaut-invision)\n\n## Chemin\n`Index` > ` Panneau d\'admnistration` > `Templates | '+template_categories[template_from_categories[tem]]+'` > `'+tem+'`\n\n## Description[*](https://fa-tvars.appspot.com/tpl/'+tem+')\n')

        if tem not in templates_desc:
            f.write('[*Ajouter une description*](https://fa-tvars.appspot.com/tpl/'+tem+')')
        else:
            f.write(templates_desc[tem])

        f.write('\n\n## Variables disponibles\n* [__Variables globales__](../../variables_globales.md#readme)\n* __Variables propres à ce template :__')

        for var in sorted(template_variables[tem], key=str.lower):
            types = list(set(r[1] for r in template_variables[tem][var]))
            for link in var2links(var, types):
                f.write('\n\t* '+link)
        
        for ver in sorted(template_versions, key=sorting_version):
            f.write('\n\n## Template par défaut '+template_versions[ver]+'\n\n[__Code source__](../src/punbb/index_box.tpl#files)\n\n### Positions des variables\n')
            for r in sorted(([r[0], r[1], var_name] for var_name in template_variables[tem] for r in template_variables[tem][var_name] if r[2] == ver), key=lambda x: x[2]):
                f.write('\n* __'+var2text(r[2], r[1])+'(../var/'+r[2]+'.md#readme) :__ ligne [`'+str(r[0])+'`](../src/'+ver+'/'+tem+'.tpl#L'+str(r[0])+')')
