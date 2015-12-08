var url = "./swagger.json";
window.swaggerUi = new SwaggerUi({
    url: url,
    dom_id: "swagger-ui-container",
    supportedSubmitMethods: [ ],
    onComplete: function(swaggerApi, swaggerUi){ },
    onFailure: function(data) { alert(data); },
    docExpansion: "list",
    validatorUrl: null,
    operationsSorter: function (a, b) {
        var aNormalized = a.path;
        var bNormalized = b.path;

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
