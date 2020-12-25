/*
 * View model for OctoPrint-Autocollapsefiles
 *
 * Author: L. Kruse
 * License: AGPLv3
 */
$(function() {
    function AutocollapsefilesViewModel(parameters) {
        var self = this;
        self.printerState = parameters[0];

        self.onStartupComplete = function(){
            self.printerState.isBusy.subscribe(function(busy) {
                if(busy){
                    if(!($('div#files_wrapper').children('div.accordion-heading').children('a.accordion-toggle').attr('class').includes('collapsed'))){
                        $('div#files_wrapper').children('div.accordion-heading').children('a.accordion-toggle').click();
                    }
                }else{
                    if($('div#files_wrapper').children('div.accordion-heading').children('a.accordion-toggle').attr('class').includes('collapsed')){
                        $('div#files_wrapper').children('div.accordion-heading').children('a.accordion-toggle').click();
                    }
                }
            })
        }
    }


    OCTOPRINT_VIEWMODELS.push({
        construct: AutocollapsefilesViewModel,
        dependencies: ['printerStateViewModel'],
        elements: []
    });
});
