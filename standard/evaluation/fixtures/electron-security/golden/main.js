const win=new BrowserWindow({webPreferences:{contextIsolation:true,sandbox:true,webSecurity:true,preload}})
session.defaultSession.setPermissionRequestHandler((wc,p,cb)=>cb(ALLOWLIST.has(p)))
win.webContents.setWindowOpenHandler(()=>({action:"deny"}))
