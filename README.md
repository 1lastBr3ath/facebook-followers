This simple python script will list out all people the user is currently following, given the token has required permission (i.e. read_stream).
"Following" people includes;<br/>
\- Friends (unless explicitly 'Unfollowed')<br/>
\- Users who you've sent friend requests to<br/>
\- People you're following

In short, the list includes people whose public feeds appear on your newsfeed.


Since Graph API version 2.0, one cannot list out all of a user's friends, even with user_friends permission. The endpoint me/friends only includes friends who also use the app, and who has also granted user_friends. Therefore, it's, now, not possible to list out all of a user's friends, in any way.

This script, however, helps list out people you're currently following, which also includes your friends. So, in some way, it lists out all of a user's friends ;)

Someone may find it useful, I hope.

TIP:<br/>
If you're not aware of API calls, don't worry. You only require an access token, which you can instantly generate via https://developers.facebook.com/toosl/explorer

There, you can find a "Get Token" button, click it, a dialog appears (as shown). Click "Extended permission", tick `read_stream`, and click "Get Access Token". Proceed through following dialogs, and a token appears right in the "Access Token" field.

<img src='http://i.imgur.com/zt6rIm5.png?1' />

<b>Usage:</b>
python followings.py &lt;access_token&gt;
