<!DOCTYPE html>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta charset="UTF-8" />
<html>
<body>
  <script type="text/javascript">
    var url=location.href;
    var _get=(url.slice(url.indexOf('?')+1, url.length));
    var userAgent = navigator.userAgent;
    if(userAgent.match(/Android/)){
      location.href='kakaotalk://inappbrowser/close';
    } else if(!userAgent.match(/Android/)&&userAgent.match(/like Mac OS X/i)) {
      setTimeout("location.href='kakaoweb://closeBrowser'",5000);
    }
    location.href=_get;
  </script>
</body>
</html>