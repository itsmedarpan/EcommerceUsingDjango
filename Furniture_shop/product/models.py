from django.db import models
from django.core.files import File

from io import BytesIO
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads', blank=True, null=True)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
    
    def get_display_price(self):
        return self.price / 100
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'
            
    # def make_thumbnail(self, image, size=(300, 300)):
    #     img = Image.open(image)
    #     img = img.convert('RGB')
    #     img.thumbnail(size) 
    #     thumb_io = BytesIO()
    #     img.save(thumb_io, 'JPEG', quality=85)  
    #     thumbnail = File(thumb_io, name=image.name) 
    #     return thumbnail

    # def make_thumbnail(self, image, size=(300, 300)):
    #     print("Making thumbnail for:", image.name)
    #     img = Image.open(image)
    #     img = img.convert('RGB')
    #     img.thumbnail(size)
    
    #     thumb_io = BytesIO()
    #     img.save(thumb_io, 'JPEG', quality=85)
    
    #     thumbnail = File(thumb_io, name=image.name)
    #     return thumbnail

    def make_thumbnail(self, image, size=(300, 300)):
        print("Making thumbnail for:", image.name)
        img = Image.open(image)
        img = img.convert('RGB')

        # Create a white background
        background = Image.new('RGB', size, (255, 255, 255))
        # Resize image to fit within size, maintaining aspect ratio
        img.thumbnail(size, Image.LANCZOS)
        # Center the image on the background
        offset = ((size[0] - img.width) // 2, (size[1] - img.height) // 2)
        background.paste(img, offset)

        thumb_io = BytesIO()
        background.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=f"thumb_{image.name}")
        return thumbnail

