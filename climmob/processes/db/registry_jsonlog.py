import os
from xml.dom import minidom

from climmob.models import RegistryJsonLog, Enumerator
from climmob.models.schema import mapToSchema, mapFromSchema

all = [
    "get_registry_logs",
    "get_error_from_log",
    "get_registry_log_by_log",
    "update_registry_status_log",
    "clean_registry_error_logs",
]


def get_registry_logs(request, projectId):

    result = mapFromSchema(
        request.dbsession.query(RegistryJsonLog, Enumerator)
        .filter(RegistryJsonLog.project_id == projectId)
        .filter(RegistryJsonLog.status == 1)
        .filter(RegistryJsonLog.enum_id == Enumerator.enum_id)
        .filter(RegistryJsonLog.enum_user == Enumerator.user_name)
        .order_by(RegistryJsonLog.log_dtime)
        .all()
    )

    for registry in result:

        registry["detail"] = get_error_from_log(registry["log_file"])
        registry["lod_dtime"] = registry["log_dtime"].strftime("%m/%d/%Y, %H:%M:%S")

    return result


def get_registry_log_by_log(request, projectId, log_id):

    result = (
        request.dbsession.query(RegistryJsonLog.json_file)
        .filter(RegistryJsonLog.project_id == projectId)
        .filter(RegistryJsonLog.status == 1)
        .filter(RegistryJsonLog.enum_user == Enumerator.user_name)
        .filter(RegistryJsonLog.enum_id == Enumerator.enum_id)
        .filter(RegistryJsonLog.log_id == log_id)
        .first()
    )

    if result:
        return True, result[0]


def update_registry_status_log(request, projectId, logid, status):
    data = {"status": status}
    mappedData = mapToSchema(RegistryJsonLog, data)
    try:
        request.dbsession.query(RegistryJsonLog).filter(
            RegistryJsonLog.project_id == projectId
        ).filter(RegistryJsonLog.log_id == logid).update(mappedData)
        return True, ""
    except Exception as e:
        print(e)
        return False, e


def get_error_from_log(inputFileLog):

    if os.path.exists(inputFileLog):
        doc = minidom.parse(inputFileLog)
        errors = doc.getElementsByTagName("error")

        return errors[0].getAttribute("Error")

    else:
        return False


def clean_registry_error_logs(request, projectId):
    try:
        request.dbsession.query(RegistryJsonLog).filter(
            RegistryJsonLog.project_id == projectId
        ).delete()
        return True, ""
    except Exception as e:
        return False, str(e)
