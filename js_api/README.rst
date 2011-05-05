==================================
 Weave Client-Side JavaScript API
==================================

Weave Client-Side JavaScript API is a high-level API built over the Session Editing API provided by Weave.

Getting started
===============

The following two JavaScript files are required and need to be loaded in your HTML document, typically inside the ``<head>`` tag:

::

    <script type="text/javascript" src="path/to/lib/swfobject/swfobject/swfobject.js"></script>
    <script type="text/javascript" src="path/to/weave.js"></script>

The function ``Weave.embed(options)`` creates a Weave Flash object on the web page. It includes ``embedSWF`` from the swfobject library, which inherits all options from ``Weave.embed(options)``. 

Example:

::

    Weave.embed({

        // path to Weave client (swf file)
        swfUrl: '/weave.swf',

        // id of the element on the web page where
        // the Weave Flash object should be added
        id: 'weavediv',

        // Weave dimensions
        width: '720',
        height: '480',
        
        // Flash specific param elements
        params : {
          // Webservice URL for Weave servlet
          base : 'http://localhost:8080/'
        }

    });

Please consult the swfobjec.embedSWF `documentation <http://code.google.com/p/swfobject/wiki/documentation#STEP_3:_Embed_your_SWF_with>`_ for a full list of valid options.

Start using the API
===================

As soon as the Weave Session Editing API becomes available, the function ``Weave.ready()`` is called. Add ``Weave.ready = function () {}`` to your document and you can start using the Weave Session Editing API.

Example:

::

    Weave.ready = function () {

        mySessionState = Weave.API.getSessionState([]);
        console.info(mySessionState);

    }

All Weave Session Editing API functions are available in form of  ``Weave.API.method`` , where *method* corresponds to a Weave Session Editing function. Please see `Weave AS Interface IExternalSessionStateInterface <http://129.63.8.210:8080/asdoc/org/openindicators/api/core/IExternalSessionStateInterface.html>`_ for more information on about the Weave Session Editing API scope. 

The global ``Weave`` object can be used to manage Weave core properties, such as the session state for instance

Example: 

::

    Weave.sessionState = Weave.API.getSessionState([]);
