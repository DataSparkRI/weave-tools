==================================
 Weave Client-Side JavaScript API
==================================

Weave Client-Side JavaScript API is a high-level API built over the session editing API provided by Weave.

Getting started
===============

The following two JavaScript files are required and need to be loaded in your HTML document, typically inside the ``<head>`` tag:

::

    <script type="text/javascript" src="path/to/lib/swfobject/swfobject/swfobject.js"></script>
    <script type="text/javascript" src="path/to/weave.js"></script>

The function ``Weave.embed(options)`` creates a Weave Flash object on the web page. It includes ``embedSWF`` from the swfobject library, which inherits all options from ``Weave.embed``. 

Example:

::

    Weave.embed({

        // path to weave.swf
        swfUrl: '/weave.swf',

        // id of the element on the web page where
        // the Weave Flash object should be added
        id: 'weavediv',

        // Weave dimensions
        width: '720',
        height: '480',

    });

Please consult the swfobjec.embedSWF `documentation <http://code.google.com/p/swfobject/wiki/documentation#STEP_3:_Embed_your_SWF_with>`_ for more information on the options argument.

Start using the API
===================

As soon as the Weave Session Editing API becomes available, the function ``Weave.ready()`` is called. Add it to your JavaScript and start using the API.

Example:

::

    Weave.ready = function () {

        mySessionState = Weave.API.getSessionState([]);
        console.info(mySessionState);

    }

All Weave Session Editing API functions are available in form of  ``Weave.API.method`` , where *method* corresponds to a Weave Session Editing function. Please see `this document <http://129.63.8.210:8080/asdoc/org/openindicators/WeaveAPI.html>`_ for more information on all Weave Session Editing function. 

The global ``Weave`` object can be used to manage Weave core properties, such as the session state for instance

Example: 

::

    Weave.sessionState = Weave.API.getSessionState([]);
