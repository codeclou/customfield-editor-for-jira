var url = "./swagger.json";
window.swaggerUi = new SwaggerUi({
    url: url,
    dom_id: "swagger-ui-container",
    supportedSubmitMethods: [ ],
    onComplete: function(swaggerApi, swaggerUi){ },
    onFailure: function(data) { alert(data); },
    docExpansion: "list",
    operationsSorter: function (a, b) {
        var aNormalized = a.path;
        var bNormalized = b.path;

        /** LEVEL 0: ALWAYS ON TOP */
        if (aNormalized.match(/^\/user\/customfields$/g) &&
            !bNormalized.match(/^\/user\/customfields$/g)) {
            return -1;
        }
        if (bNormalized.match(/^\/user\/customfields\/\{customFieldId\}\/contexts$/g) &&
            !aNormalized.match(/^\/user\/customfields\/\{customFieldId\}\/contexts$/g)) {
            return 1;
        }

        /** LEVEL 1: CONTEXT DEFAULT */
        if (aNormalized.match(/\/contexts\/default\//g) &&
            !bNormalized.match(/\/contexts\/default\//g )) {
            return 1;
        }
        if (bNormalized.match(/\/contexts\/default\//g) &&
            !aNormalized.match(/\/contexts\/default\//g )) {
            return -1;
        }

        /** LEVEL 1.X: CHILDOPTIONS */
        if (aNormalized.match(/\/childoptions\//g) &&
            !bNormalized.match(/\/childoptions\//g) ) {
            return 1;
        }
        if (bNormalized.match(/\/childoptions\//g) &&
            !aNormalized.match(/\/childoptions\//g) ) {
            return -1;
        }

        /** NORMAL COMPARISON */
        if (aNormalized.length > bNormalized.length) {
            return 1;
        }
        if (aNormalized.length < bNormalized.length) {
            return -1;
        }
        return 0;
    },
    withCredentials: false
});
window.swaggerUi.load();
