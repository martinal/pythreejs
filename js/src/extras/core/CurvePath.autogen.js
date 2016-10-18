//
// This file auto-generated with generate-wrappers.js
// Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT)
//

var _ = require('underscore');
var widgets = require('jupyter-js-widgets');

var ThreeModel = require('../../_base/Three').ThreeModel;
var ThreeView = require('../../_base/Three').ThreeView;


var CurvePathModel = ThreeModel.extend({

    defaults: _.extend({}, ThreeModel.prototype.defaults, {

        _view_name: 'CurvePathView',
        _model_name: 'CurvePathModel',


    }),

    constructThreeObject: function() {

        return new THREE.CurvePath();

    },

    createPropertiesArrays: function() {

        ThreeModel.prototype.createPropertiesArrays.call(this);

    },

});

var CurvePathView = ThreeView.extend({});

module.exports = {
    CurvePathView: CurvePathView,
    CurvePathModel: CurvePathModel,
};