<!-- BEGIN switch_user_logged_in -->
<div id="pun-visit" class="clearfix">
	<ul>
	 	<li><a href="{U_SEARCH_NEW}">{L_SEARCH_NEW}</a></li>
	 	<li><a href="{U_SEARCH_SELF}">{L_SEARCH_SELF}</a></li>
	</ul>
	<p>{LOGGED_AS}. {LAST_VISIT_DATE}</p>
</div>
<!-- END switch_user_logged_in -->
<!-- BEGIN switch_user_logged_out -->
<div id="pun-visit">
	<p>{L_NOT_CONNECTED} {L_LOGIN_REGISTER}</p>
</div>
<!-- END switch_user_logged_out -->
<div class="pun-crumbs">
	<p class="crumbs"><a href="{U_INDEX}">{L_INDEX}</a> <strong>&raquo; {L_CALENDAR}</strong></p>
</div>

<div class="main">
<form name="_calendar" method="post" action="{S_ACTION}" class="frm-form">
	{CALENDAR_MONTH}
</form>
</div>