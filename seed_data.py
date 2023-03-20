from SocialTravel.models import Post
# Post(carousel_caption_title="Un carousel title4",
#      carousel_caption_description="Un carousel descript4",
#      heading="un viaje4",
#      description="Una dewscripcion4",
#      ).save()
# Post(carousel_caption_title="Un carousel title5",
#      carousel_caption_description="Un carousel descript5",
#      heading="un viaje5",
#      description="Una dewscripcion5",
#      ).save()
for _ in range(0, 100):
    Post(carousel_caption_title="Un Carousel Title",
    carousel_caption_description="Un carousel descript",
    heading="Mi viaje",
    description="una description",
    #un_campo=""
    ).save()
