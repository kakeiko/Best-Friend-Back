import requests
import os
from dotenv import load_dotenv
from .models import DogBreed

load_dotenv()
def uptadeDogBreed():
    apiLink = os.getenv('API_LINK_INFO')
    apiKey = os.getenv('API_KEY')

    headers = {
        "x-api-key": apiKey
    }

    page = 0
    limit = 50

    while True:
        response = requests.get(
            f"{apiLink}?limit={limit}&page={page}",
            headers=headers
        )

        data = response.json()

        if not data:
            break

        for breed in data:
            try: 
                name = breed['name']
                origin = breed['origin']
                group = breed['breed_group']
                life_span = breed['life_span']
                temperament = breed['temperament']
                weight = breed['weight']['metric']
                height = breed['height']['metric']
                description = breed['description']

                dogBreedCreate = DogBreed.objects.create(
                    name=name,
                    origin=origin,
                    group=group,
                    life_span=life_span,
                    temperament=temperament,
                    weight=weight,
                    height=height,
                    description=description,
                )

                dogBreedCreate.save()
            except Exception as error:
                print(error)

        page += 1