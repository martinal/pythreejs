//
// This file auto-generated with generate-wrappers.js
// Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT)
//

var _ = require('underscore');
var widgets = require('jupyter-js-widgets');

var ThreeModel = require('../_base/Three').ThreeModel;
var ThreeView = require('../_base/Three').ThreeView;


var Line3Model = ThreeModel.extend({

    defaults: _.extend({}, ThreeModel.prototype.defaults, {

        _view_name: 'Line3View',
        _model_name: 'Line3Model',

        start: [0,0,0],
        end: [0,0,0],

    }),

    constructThreeObject: function() {

        return new THREE.Line3(
            this.get('start'),
            this.get('end')
        );

    },

    createPropertiesArrays: function() {

        ThreeModel.prototype.createPropertiesArrays.call(this);
        this.vector_properties.push('start');
        this.vector_properties.push('end');

    },

});

var Line3View = ThreeView.extend({});

module.exports = {
    Line3View: Line3View,
    Line3Model: Line3Model,
};