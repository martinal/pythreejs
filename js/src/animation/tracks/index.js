//
// This file auto-generated with generate-wrappers.js
// Date: Tue Oct 18 2016 14:57:28 GMT-0700 (PDT)
//
// Load all three.js python wrappers
var loadedModules = [
    require('./BooleanKeyframeTrack.autogen.js'),
    require('./ColorKeyframeTrack.autogen.js'),
    require('./NumberKeyframeTrack.autogen.js'),
    require('./QuaternionKeyframeTrack.autogen.js'),
    require('./StringKeyframeTrack.autogen.js'),
    require('./VectorKeyframeTrack.autogen.js'),
];

for (var i in loadedModules) {
    if (loadedModules.hasOwnProperty(i)) {
        var loadedModule = loadedModules[i];
        for (var target_name in loadedModule) {
            if (loadedModule.hasOwnProperty(target_name)) {
                module.exports[target_name] = loadedModule[target_name];
            }
        }
    }
}
