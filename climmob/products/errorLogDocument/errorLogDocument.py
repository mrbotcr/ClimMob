from climmob.products.climmob_products import (
    createProductDirectory,
    registerProductInstance,
)
from climmob.products.errorLogDocument.celerytasks import createErrorLogDocument

# This function has been declated in climmob.plugins.interfaces.IPackage#after_create_packages
def create_error_log_document(
    request,
    locale,
    userOwner,
    projectId,
    projectCod,
    form,
    code,
    structure,
    listOfErrors,
    info,
):
    # We create the plugin directory if it does not exists and return it
    # The path user.repository in development.ini/user/project/products/product and
    # user.repository in development.ini/user/project/products/product/outputs

    path = createProductDirectory(request, userOwner, projectCod, "errorlogdocument")
    # We call the Celery task that will generate the output packages.pdf
    task = createErrorLogDocument.apply_async(
        (
            locale,
            userOwner,
            path,
            projectCod,
            form,
            code,
            structure,
            listOfErrors,
            info,
        ),
        queue="ClimMob",
    )
    # We register the instance of the output with the task ID of celery
    # This will go to the products table that then you can monitor and use
    # in the nice product interface
    nameOutput = form + "_form"
    if code != "":
        nameOutput += "_" + code

    registerProductInstance(
        projectId,
        "errorlogdocument",
        nameOutput + "_" + projectCod + ".xlsx",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "create_errorlog_" + form + "_" + code,
        task.id,
        request,
    )
