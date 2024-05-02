import json

from pyramid.response import Response

from climmob.processes import (
    getTechsAlias,
    findTechalias,
    addTechAlias,
    updateAlias,
    removeAlias,
    existAlias,
    getAliasAssignedWithoutProjectCode,
    getTechnologyByUser,
)
from climmob.views.classes import apiView


class createAlias_view(apiView):
    def processView(self):

        if self.request.method == "POST":

            obligatory = ["tech_id", "alias_name"]
            dataworking = json.loads(self.body)

            if sorted(obligatory) == sorted(dataworking.keys()):

                dataInParams = True
                for key in dataworking.keys():
                    if dataworking[key] == "":
                        dataInParams = False

                if dataInParams:
                    dataworking["user_name"] = self.user.login
                    dataworking["alias_id"] = None
                    if getTechnologyByUser(dataworking, self.request):

                        existAlias = findTechalias(dataworking, self.request)
                        if existAlias == False:
                            added, message = addTechAlias(
                                dataworking, self.request, "API"
                            )
                            if not added:
                                response = Response(status=401, body=message)
                                return response
                            else:
                                response = Response(
                                    status=200, body=json.dumps(message)
                                )
                                return response
                        else:
                            response = Response(
                                status=401,
                                body=self._(
                                    "This technology option already exists in the technology."
                                ),
                            )
                            return response
                    else:
                        response = Response(
                            status=401,
                            body=self._("You do not have a technology with this ID."),
                        )
                        return response

                else:
                    response = Response(
                        status=401, body=self._("Not all parameters have data.")
                    )
                    return response
            else:
                response = Response(status=401, body=self._("Error in the JSON."))
                return response
        else:
            response = Response(status=401, body=self._("Only accepts POST method."))
            return response


class readAlias_view(apiView):
    def processView(self):
        if self.request.method == "GET":
            obligatory = ["tech_id"]
            try:
                dataworking = json.loads(self.body)
            except:
                response = Response(status=401, body=self._("Error in the JSON."))
                return response
            if sorted(obligatory) == sorted(dataworking.keys()):

                dataInParams = True
                for key in dataworking.keys():
                    if dataworking[key] == "":
                        dataInParams = False

                if dataInParams:
                    dataworking["user_name"] = self.user.login
                    if getTechnologyByUser(dataworking, self.request):

                        response = Response(
                            status=200,
                            body=json.dumps(
                                getTechsAlias(dataworking["tech_id"], self.request)
                            ),
                        )
                        return response
                    else:
                        dataworking["user_name"] = "bioversity"
                        if getTechnologyByUser(dataworking, self.request):

                            response = Response(
                                status=200,
                                body=json.dumps(
                                    getTechsAlias(dataworking["tech_id"], self.request)
                                ),
                            )
                            return response
                        else:
                            response = Response(
                                status=401,
                                body=self._("There is no technology with this ID."),
                            )
                            return response
                else:
                    response = Response(
                        status=401, body=self._("Not all parameters have data.")
                    )
                    return response
            else:
                response = Response(status=401, body=self._("Error in the JSON."))
                return response
        else:
            response = Response(status=401, body=self._("Only accepts GET method."))
            return response


class updateAlias_view(apiView):
    def processView(self):
        if self.request.method == "POST":

            obligatory = ["tech_id", "alias_id", "alias_name"]
            dataworking = json.loads(self.body)

            if sorted(obligatory) == sorted(dataworking.keys()):

                dataInParams = True
                for key in dataworking.keys():
                    if dataworking[key] == "":
                        dataInParams = False

                if dataInParams:
                    dataworking["user_name"] = self.user.login
                    if getTechnologyByUser(dataworking, self.request):
                        if existAlias(dataworking, self.request):
                            existAlias2 = findTechalias(dataworking, self.request)
                            if existAlias2 == False:
                                if not getAliasAssignedWithoutProjectCode(
                                    dataworking, self.request
                                ):
                                    update, message = updateAlias(
                                        dataworking, self.request
                                    )
                                    if not update:
                                        response = Response(status=401, body=message)
                                        return response
                                    else:
                                        response = Response(
                                            status=200,
                                            body=self._(
                                                "The technology option was updated successfully."
                                            ),
                                        )
                                        return response
                                else:
                                    response = Response(
                                        status=401,
                                        body=self._(
                                            "You can not update this technology option because it has been assigned to a project."
                                        ),
                                    )
                                    return response
                            else:
                                response = Response(
                                    status=401,
                                    body=self._(
                                        "This technology option already exists for the technology."
                                    ),
                                )
                                return response
                        else:
                            response = Response(
                                status=401,
                                body=self._(
                                    "You do not have a technology option with this ID."
                                ),
                            )
                            return response
                    else:
                        response = Response(
                            status=401,
                            body=self._("You do not have a technology with this ID."),
                        )
                        return response

                else:
                    response = Response(
                        status=401, body=self._("Not all parameters have data.")
                    )
                    return response
            else:
                response = Response(status=401, body=self._("Error in the JSON."))
                return response
        else:
            response = Response(status=401, body=self._("Only accepts POST method."))
            return response


class deleteAliasView_api(apiView):
    def processView(self):

        if self.request.method == "POST":

            obligatory = ["tech_id", "alias_id"]
            dataworking = json.loads(self.body)

            if sorted(obligatory) == sorted(dataworking.keys()):

                dataInParams = True
                for key in dataworking.keys():
                    if dataworking[key] == "":
                        dataInParams = False

                if dataInParams:
                    dataworking["user_name"] = self.user.login
                    if getTechnologyByUser(dataworking, self.request):
                        if existAlias(dataworking, self.request):
                            if not getAliasAssignedWithoutProjectCode(
                                dataworking, self.request
                            ):
                                removed, message = removeAlias(
                                    dataworking, self.request
                                )
                                if not removed:
                                    response = Response(status=401, body=message)
                                    return response
                                else:
                                    response = Response(
                                        status=200,
                                        body=self._(
                                            "The technology option was deleted successfully."
                                        ),
                                    )
                                    return response
                            else:
                                response = Response(
                                    status=401,
                                    body=self._(
                                        "You cannot delete this technology option because it has been assigned to a project."
                                    ),
                                )
                                return response
                        else:
                            response = Response(
                                status=401,
                                body=self._("You do not have a alias with this ID."),
                            )
                            return response
                    else:
                        response = Response(
                            status=401,
                            body=self._("You do not have a technology with this ID."),
                        )
                        return response

                else:
                    response = Response(
                        status=401, body=self._("Not all parameters have data.")
                    )
                    return response
            else:
                response = Response(status=401, body=self._("Error in the JSON."))
                return response
        else:
            response = Response(status=401, body=self._("Only accepts POST method."))
            return response
