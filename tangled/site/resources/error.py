from tangled.web import Resource, represent


TITLES = {
    400: "Bad request",
    403: "You're not allowed to do that",
    404: "That page wasn't found",
    405: "That operation isn't supported",
    500: 'Something unexpected happened',
}


DETAILS = {

}


class Error(Resource):

    @represent('text/html', template_name='error.mako')
    def GET(self):
        request = self.request
        response = request.response
        if response.status_code == 401:
            location = request.make_url('/sign-in')
            request.abort(307, location=location)
        else:
            return {
                'title': TITLES.get(response.status_code, 'Error'),
                'detail': DETAILS.get(response.status_code, '')
            }
