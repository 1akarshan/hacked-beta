'use strict';

var tslib = require('tslib');
var i0 = require('@angular/core');
var core = require('@awesome-cordova-plugins/core');
require('rxjs');

function _interopNamespaceDefault(e) {
    var n = Object.create(null);
    if (e) {
        Object.keys(e).forEach(function (k) {
            if (k !== 'default') {
                var d = Object.getOwnPropertyDescriptor(e, k);
                Object.defineProperty(n, k, d.get ? d : {
                    enumerable: true,
                    get: function () { return e[k]; }
                });
            }
        });
    }
    n.default = e;
    return Object.freeze(n);
}

var i0__namespace = /*#__PURE__*/_interopNamespaceDefault(i0);

var MediaCapture = /** @class */ (function (_super) {
    tslib.__extends(MediaCapture, _super);
    function MediaCapture() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    MediaCapture.prototype.captureAudio = function (options) { return core.cordova(this, "captureAudio", { "callbackOrder": "reverse" }, arguments); };
    MediaCapture.prototype.captureImage = function (options) { return core.cordova(this, "captureImage", { "callbackOrder": "reverse" }, arguments); };
    MediaCapture.prototype.captureVideo = function (options) { return core.cordova(this, "captureVideo", { "callbackOrder": "reverse" }, arguments); };
    MediaCapture.prototype.onPendingCaptureResult = function () { return core.cordova(this, "onPendingCaptureResult", { "eventObservable": true, "event": "pendingcaptureresult" }, arguments); };
    MediaCapture.prototype.onPendingCaptureError = function () { return core.cordova(this, "onPendingCaptureError", { "eventObservable": true, "event": "pendingcaptureerror" }, arguments); };
    Object.defineProperty(MediaCapture.prototype, "supportedImageModes", {
        get: function () { return core.cordovaPropertyGet(this, "supportedImageModes"); },
        set: function (value) { core.cordovaPropertySet(this, "supportedImageModes", value); },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(MediaCapture.prototype, "supportedAudioModes", {
        get: function () { return core.cordovaPropertyGet(this, "supportedAudioModes"); },
        set: function (value) { core.cordovaPropertySet(this, "supportedAudioModes", value); },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(MediaCapture.prototype, "supportedVideoModes", {
        get: function () { return core.cordovaPropertyGet(this, "supportedVideoModes"); },
        set: function (value) { core.cordovaPropertySet(this, "supportedVideoModes", value); },
        enumerable: false,
        configurable: true
    });
    MediaCapture.ɵfac = i0__namespace.ɵɵngDeclareFactory({ minVersion: "12.0.0", version: "12.2.16", ngImport: i0__namespace, type: MediaCapture, deps: null, target: i0__namespace.ɵɵFactoryTarget.Injectable });
    MediaCapture.ɵprov = i0__namespace.ɵɵngDeclareInjectable({ minVersion: "12.0.0", version: "12.2.16", ngImport: i0__namespace, type: MediaCapture });
    MediaCapture.pluginName = "MediaCapture";
    MediaCapture.plugin = "cordova-plugin-media-capture";
    MediaCapture.pluginRef = "navigator.device.capture";
    MediaCapture.repo = "https://github.com/apache/cordova-plugin-media-capture";
    MediaCapture.platforms = ["Android", "Browser", "iOS", "Windows"];
    MediaCapture = tslib.__decorate([], MediaCapture);
    return MediaCapture;
}(core.AwesomeCordovaNativePlugin));
i0__namespace.ɵɵngDeclareClassMetadata({ minVersion: "12.0.0", version: "12.2.16", ngImport: i0__namespace, type: MediaCapture, decorators: [{
            type: i0.Injectable
        }], propDecorators: { supportedImageModes: [], supportedAudioModes: [], supportedVideoModes: [], captureAudio: [], captureImage: [], captureVideo: [], onPendingCaptureResult: [], onPendingCaptureError: [] } });

exports.MediaCapture = MediaCapture;
