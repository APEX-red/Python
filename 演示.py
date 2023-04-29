<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Webos</title>
    <meta name="referrer" content="never">
    <link rel="manifest" href="./win11.manifest.json"/>
    <script>"serviceWorker" in navigator&&window.addEventListener("load",(()=>{navigator.serviceWorker.register("./serviceWorker.js").then((e=>console.log("Success: ",e.scope))).catch((e=>console.log("Failure: ",e)))}))</script>
    <script src="./modules/win11/init.js?from=element&plugins=win11"></script>
</head>
<body style="display:none;" data-theme="light" data-sepia="false">
<div id="app">
    <app ref="app"></app>
</div>
</body>
<script>
    (function(){
        let version = window&&window.utils&&window.utils.config&&window.utils.config.version;
        if(!version){
            version = "1.0.0";
        }
        window.InitVueComponent = function (app){
            var zjs = ["app","folder-tree","edgeBrowser","taskbar","window","desktop","right-menu","fileExplorer","login",
                "settings","settings-user","store","commonApp","properties","upload-task","personal","file-select",
                "settings-webdav","settings-system","settings-update","settings-business","settings-sponsor","settings-dbcache",
                "settings-offlinedown","settings-log"];
            for(let i=0;i<zjs.length;i++){
                let zj = zjs[i];
                app.component(zj, Vue.defineAsyncComponent(function (){
                    return import('./modules/win11/components/'+zj+'.js?jsv='+version);
                }));
            }
        };
        utils.delayAction(function (){
            return window && window.webos && window.webos.user;
        },function (){
            Vue.app({
                mounted:function(){
                    document.body.style.display = "";
                    utils.delayAction(function (){
                        return window.webos && webos.context && webos.context.get("install") != undefined;
                    },function (){
                        if(!webos.context.get("install")){
                            window.location.href = "install.html";
                        }
                    });
                }
            });
        });
    })()
</script>
</html>