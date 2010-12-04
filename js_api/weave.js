(function() {
  
  window.Weave = {
    
    /*
     * Embed a custom Weave Flash object.
     */
    
    embed: function (options) {
      
      /*
       * Default Weave Flash options.
       */
      
      this.swfUrl = 'http://localhost:8080/weave.swf';
      this.id = 'weavediv';
      this.width = '720';
      this.height = '480';
      this.version = '9.0.0';
      this.expressInstallSwfurl = 'lib/swfobject/swfobject/expressInstall.swf';
      this.flashvars = {};
      this.params = {
        quality : 'high',
        bgcolor : '#ffffff',
        allowfullscreen : 'true',
        allowscriptaccess : 'always',
        base : 'http://localhost:8080/'
      };
      this.attributes = {};
 
      /*
       * Overriding default with custom options.
       */
      
      for (var option in options) {
        
        this[option] = options[option];
        
        /*
         * FIXME: check if option is object and only override 
         * single properties instead of entire object.
         */
        
      }
      
      /*
       * Embed the Weave Flash object with swfobject.
       */
       
      swfobject.embedSWF(
        this.swfUrl, 
        this.id, 
        this.width,
        this.height,
        this.version,
        this.expressInstallSwfurl,
        this.flashvars, 
        this.params, 
        this.attributes,
        function(e) {
          if(e.success) {
            
            /*
             * Check (every second) if Weave API is available.
             * We don't have a better option yet...
             */
            
            setTimeout('Weave.checkAPI()', 1000);
          }
        }
      );
    },
    
    /*
     * Check if Weave Session Editing API is available.
     */
    
    checkAPI: function () {
      
      try {
        
        /*
         * Weave Session Editing API
         */
         
        Weave.API = document.getElementById(this.id);
        
        /*
         * Returns no error as soon as API is available.
         */
        
        this.sessionState = Weave.API.getSessionState([]);
        
        /*
         * Reset sessionState property.
         */
        
        this.sessionState = null;
        
        /*
         * Weave is ready to use.
         */
         
         Weave.ready();
        
      }
      catch (err) {
        setTimeout('Weave.checkAPI()', 1000);
      }
    }
 
  };

})();
