# switch_privmsg
* __Type__ __:__ variable de bouclage
* __Utilisable dans__ __:__ [`posting_body`](../tpl/posting_body.md#readme)
* __Utilisation__ __:__

```smarty
<!-- BEGIN switch_privmsg -->
contenu sur lequel on boucle
<!-- END switch_privmsg -->
```

## Description[*](https://fa-tvars.appspot.com/var/switch_privmsg)
[*Ajouter une description*](https://fa-tvars.appspot.com/var/switch_privmsg)

## Attributs
* __&nbsp;&nbsp;&nbsp;&nbsp;[`<!-- BEGIN switch_privmsg_friend -->`](../var/switch_privmsg.switch_privmsg_friend.md#readme) ([x](https://fa-tvars.appspot.com/var/switch_privmsg.switch_privmsg_friend))__
* __&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[`{switch_privmsg.switch_privmsg_friend.FRIEND_PM}`](../var/switch_privmsg.switch_privmsg_friend.FRIEND_PM.md#readme) ([x](https://fa-tvars.appspot.com/var/switch_privmsg.switch_privmsg_friend.FRIEND_PM))__
* __&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[`{switch_privmsg.switch_privmsg_friend.L_OR_FRIEND}`](../var/switch_privmsg.switch_privmsg_friend.L_OR_FRIEND.md#readme) ([x](https://fa-tvars.appspot.com/var/switch_privmsg.switch_privmsg_friend.L_OR_FRIEND))__
* __&nbsp;&nbsp;&nbsp;&nbsp;[`<!-- BEGIN switch_privmsg_group -->`](../var/switch_privmsg.switch_privmsg_group.md#readme) ([x](https://fa-tvars.appspot.com/var/switch_privmsg.switch_privmsg_group))__
* __&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[`{switch_privmsg.switch_privmsg_group.L_OR_GROUP}`](../var/switch_privmsg.switch_privmsg_group.L_OR_GROUP.md#readme) ([x](https://fa-tvars.appspot.com/var/switch_privmsg.switch_privmsg_group.L_OR_GROUP))__
* __&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[`{switch_privmsg.switch_privmsg_group.MASS_PM}`](../var/switch_privmsg.switch_privmsg_group.MASS_PM.md#readme) ([x](https://fa-tvars.appspot.com/var/switch_privmsg.switch_privmsg_group.MASS_PM))__
* __&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[`{switch_privmsg.switch_privmsg_group.MASS_PM_EXPLAIN}`](../var/switch_privmsg.switch_privmsg_group.MASS_PM_EXPLAIN.md#readme) ([x](https://fa-tvars.appspot.com/var/switch_privmsg.switch_privmsg_group.MASS_PM_EXPLAIN))__
* __&nbsp;&nbsp;&nbsp;&nbsp;[`<!-- BEGIN switch_username -->`](../var/switch_privmsg.switch_username.md#readme) ([x](https://fa-tvars.appspot.com/var/switch_privmsg.switch_username))__
* __&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[`{switch_privmsg.switch_username.USERNAME}`](../var/switch_privmsg.switch_username.USERNAME.md#readme) ([x](https://fa-tvars.appspot.com/var/switch_privmsg.switch_username.USERNAME))__


## Utilisations dans les templates

### Version phpBB3
* __[`posting_body`](../tpl/posting_body.md#readme)__ __:__ lignes [`64`](../src/prosilver/posting_body.tpl#L64)[`<->`](../src/prosilver/posting_body.tpl#L64-L88)[`88`](../src/prosilver/posting_body.tpl#L88), [`406`](../src/prosilver/posting_body.tpl#L406)[`<->`](../src/prosilver/posting_body.tpl#L406-L411)[`411`](../src/prosilver/posting_body.tpl#L411), [`415`](../src/prosilver/posting_body.tpl#L415)[`<->`](../src/prosilver/posting_body.tpl#L415-L417)[`417`](../src/prosilver/posting_body.tpl#L417)

### Version phpBB2
* __[`posting_body`](../tpl/posting_body.md#readme)__ __:__ lignes [`102`](../src/subsilver/posting_body.tpl#L102)[`<->`](../src/subsilver/posting_body.tpl#L102-L128)[`128`](../src/subsilver/posting_body.tpl#L128), [`608`](../src/subsilver/posting_body.tpl#L608)[`<->`](../src/subsilver/posting_body.tpl#L608-L612)[`612`](../src/subsilver/posting_body.tpl#L612), [`616`](../src/subsilver/posting_body.tpl#L616)[`<->`](../src/subsilver/posting_body.tpl#L616-L618)[`618`](../src/subsilver/posting_body.tpl#L618)

### Version ModernBB
* __[`posting_body`](../tpl/posting_body.md#readme)__ __:__ lignes [`60`](../src/modernbb/posting_body.tpl#L60)[`<->`](../src/modernbb/posting_body.tpl#L60-L84)[`84`](../src/modernbb/posting_body.tpl#L84), [`401`](../src/modernbb/posting_body.tpl#L401)[`<->`](../src/modernbb/posting_body.tpl#L401-L406)[`406`](../src/modernbb/posting_body.tpl#L406), [`410`](../src/modernbb/posting_body.tpl#L410)[`<->`](../src/modernbb/posting_body.tpl#L410-L412)[`412`](../src/modernbb/posting_body.tpl#L412)

### Version PunBB
* __[`posting_body`](../tpl/posting_body.md#readme)__ __:__ lignes [`83`](../src/punbb/posting_body.tpl#L83)[`<->`](../src/punbb/posting_body.tpl#L83-L107)[`107`](../src/punbb/posting_body.tpl#L107), [`421`](../src/punbb/posting_body.tpl#L421)[`<->`](../src/punbb/posting_body.tpl#L421-L425)[`425`](../src/punbb/posting_body.tpl#L425), [`429`](../src/punbb/posting_body.tpl#L429)[`<->`](../src/punbb/posting_body.tpl#L429-L431)[`431`](../src/punbb/posting_body.tpl#L431)

### Version Invision
* __[`posting_body`](../tpl/posting_body.md#readme)__ __:__ lignes [`60`](../src/invision/posting_body.tpl#L60)[`<->`](../src/invision/posting_body.tpl#L60-L90)[`90`](../src/invision/posting_body.tpl#L90), [`369`](../src/invision/posting_body.tpl#L369)[`<->`](../src/invision/posting_body.tpl#L369-L373)[`373`](../src/invision/posting_body.tpl#L373), [`377`](../src/invision/posting_body.tpl#L377)[`<->`](../src/invision/posting_body.tpl#L377-L379)[`379`](../src/invision/posting_body.tpl#L379)

