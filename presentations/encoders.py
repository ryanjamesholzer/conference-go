from common.json import ModelEncoder
from .models import Presentation
from events.encoders import ConferenceListEncoder


class PresentationDetailEncoder(ModelEncoder):
    model = Presentation
    properties = [
        "presenter_name",
        "company_name",
        "presenter_email",
        "title",
        "synopsis",
        "created",
        "conference",
    ]

    def get_extra_data(self, o):
        return {
            "status": o.status.name,
        }

    encoders = {
        "conference": ConferenceListEncoder(),
    }


class PresentationListEncoder(ModelEncoder):
    model = Presentation
    properties = [
        "title",
    ]

    def get_extra_data(self, o):
        return {"status": o.status.name}
