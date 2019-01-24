from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
import datetime
from market.models import *


class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
        
    def test_user(self):
        user = authenticate(username='username', password='password')
        check = user is not None
        self.assertEquals(False, check)

    def test_user_real(self):
        user = authenticate(username='john', password='glass onion')
        check = user is not None
        self.assertEquals(True, check)

    def test_user_email(self):
        user = authenticate(email='jlennon@beatles.com', password='glass onion')
        check = user is not None
        self.assertEquals(False, check)

    def test_user_wrongpassword(self):
        user = authenticate(username='john', password='GLASS ONION')
        check = user is not None
        self.assertEquals(False, check)



# class Shop(models.Model):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     ShopOwner = models.CharField(max_length=255)
#     ShopName = models.CharField(max_length=255)
#     Address = models.CharField(max_length=255)
#     NumOfAds = models.IntegerField()
#     NumOfQuickAds = models.IntegerField()
#     ProfilePic = models.ImageField(upload_to="profilePics/")

#     CreatedAt = models.DateField(auto_now_add=True)
#     shop_category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
#     hash_tags = models.ManyToManyField(HashTag)
#     open_days = models.ManyToManyField(Day)
#     zip_code = models.ForeignKey(ZIPCode, on_delete=models.CASCADE)




class ShopModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
        HashTag.objects.create(tag_name='clothes')
        ShopCategory.objects.create(category_name='salons')
        shop_category = ShopCategory.objects.get(id=1)
        hashtag = HashTag.objects.get(id=1)
        shop_category.allowed_hash_tags.add(hashtag) 
        Day.objects.create(day_name='today')  
        day = Day.objects.get(id=1)        
        ZIPCode.objects.create(District='Kandy', City='Peradeniya', Code='20400')     
        zip_code = ZIPCode.objects.get(id=1)
        shop = Shop.objects.create(user=user, ShopOwner='ShopOwner', ShopName='ShopName', Address='Address',
                             NumOfAds=5, NumOfQuickAds=3, ProfilePic='path', shop_category=shop_category, zip_code=zip_code)
        shop.hash_tags.add(hashtag)
        shop.open_days.add(day)


    def test_shop_address(self):
        shop = Shop.objects.get(id=1)
        field_label = shop._meta.get_field('Address').verbose_name
        self.assertEquals(field_label, 'Address')


    def test_shop_ShopOwner(self):
        shop = Shop.objects.get(id=1)
        field_label = shop._meta.get_field('ShopOwner').verbose_name
        self.assertEquals(field_label, 'ShopOwner')


    def test_shop_NumOfAds(self):
        shop = Shop.objects.get(id=1)
        NumOfAds = shop.NumOfAds
        self.assertEquals(NumOfAds, 5)


    def test_shop_NumOfQuickAds(self):
        shop = Shop.objects.get(id=1)
        NumOfQuickAds = shop.NumOfQuickAds
        self.assertEquals(NumOfQuickAds, 3)


    def test_shop_ProfilePic(self):
        shop = Shop.objects.get(id=1)
        field_label = shop._meta.get_field('ProfilePic').verbose_name
        self.assertEquals(field_label, 'ProfilePic')


    def test_shop_shop_category(self):
        shop = Shop.objects.get(id=1)
        field_label = shop._meta.get_field('shop_category').verbose_name
        self.assertEquals(field_label, 'shop category')


    def test_shop_hash_tags(self):
        shop = Shop.objects.get(id=1)
        field_label = shop._meta.get_field('hash_tags').verbose_name
        self.assertEquals(field_label, 'hash tags')


    def test_shop_open_days(self):
        shop = Shop.objects.get(id=1)
        field_label = shop._meta.get_field('open_days').verbose_name
        self.assertEquals(field_label, 'open days')


# class Advertisement(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
#     Advertisement_text = models.CharField(max_length=255)
#     Advertisement_data = models.ImageField(upload_to="adds/")
#     hash_tags = models.ManyToManyField(HashTag, blank=True)
#     CreatedAt = models.DateField(auto_now_add=True)
#     def __str__(self):
#         return self.Advertisement_text




class AdvertisementModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
        HashTag.objects.create(tag_name='clothes')
        ShopCategory.objects.create(category_name='salons')
        shop_category = ShopCategory.objects.get(id=1)
        hashtag = HashTag.objects.get(id=1)
        shop_category.allowed_hash_tags.add(hashtag) 
        Day.objects.create(day_name='today')  
        day = Day.objects.get(id=1)        
        ZIPCode.objects.create(District='Kandy', City='Peradeniya', Code='20400')     
        zip_code = ZIPCode.objects.get(id=1)
        shop = Shop.objects.create(user=user, ShopOwner='ShopOwner', ShopName='ShopName', Address='Address',
                             NumOfAds=5, NumOfQuickAds=3, ProfilePic='path', shop_category=shop_category, zip_code=zip_code)
        shop.hash_tags.add(hashtag)
        shop.open_days.add(day)

        add = Advertisement.objects.create(shop=shop, Advertisement_text='Advertisement_text', Advertisement_data='Advertisement_data')


    def test_add_shop(self):
        add = Advertisement.objects.get(id=1)
        field_label = add._meta.get_field('shop').verbose_name
        self.assertEquals(field_label, 'shop')


    def test_add_Advertisement_text(self):
        add = Advertisement.objects.get(id=1)
        field_label = add._meta.get_field('Advertisement_text').verbose_name
        self.assertEquals(field_label, 'Advertisement text')


    def test_add_Advertisement_data(self):
        add = Advertisement.objects.get(id=1)
        field_label = add._meta.get_field('Advertisement_data').verbose_name
        self.assertEquals(field_label, 'Advertisement data')


# class QuickAdd(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
#     QuickAdd_text = models.CharField(max_length=255)
#     QuickAdd_data = models.ImageField(upload_to="quick_adds/")
#     hash_tags = models.ManyToManyField(HashTag, blank=True)
#     CreatedAt = models.DateField(auto_now_add=True, db_index=True)
#     def __str__(self):
#         return "QuickAdd: "+self.QuickAdd_text


class QuickAddModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
        HashTag.objects.create(tag_name='clothes')
        ShopCategory.objects.create(category_name='salons')
        shop_category = ShopCategory.objects.get(id=1)
        hashtag = HashTag.objects.get(id=1)
        shop_category.allowed_hash_tags.add(hashtag) 
        Day.objects.create(day_name='today')  
        day = Day.objects.get(id=1)        
        ZIPCode.objects.create(District='Kandy', City='Peradeniya', Code='20400')     
        zip_code = ZIPCode.objects.get(id=1)
        shop = Shop.objects.create(user=user, ShopOwner='ShopOwner', ShopName='ShopName', Address='Address',
                             NumOfAds=5, NumOfQuickAds=3, ProfilePic='path', shop_category=shop_category, zip_code=zip_code)
        shop.hash_tags.add(hashtag)
        shop.open_days.add(day)

        add = QuickAdd.objects.create(shop=shop, QuickAdd_text='QuickAdd_text', QuickAdd_data='QuickAdd_data')


    def test_shop_shop(self):
        qadd = QuickAdd.objects.get(id=1)
        field_label = qadd._meta.get_field('shop').verbose_name
        self.assertEquals(field_label, 'shop')


    def test_QuickAdd_text(self):
        qadd = QuickAdd.objects.get(id=1)
        field_label = qadd._meta.get_field('QuickAdd_text').verbose_name
        self.assertEquals(field_label, 'QuickAdd text')

    def test_QuickAdd_data(self):
        qadd = QuickAdd.objects.get(id=1)
        field_label = qadd._meta.get_field('QuickAdd_data').verbose_name
        self.assertEquals(field_label, 'QuickAdd data')


# class Customer(models.Model):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     followed_shops = models.ManyToManyField(Shop, blank=True)
#     timestamp = models.DateTimeField()

#     def __str__(self):
#         return str(self.user.username)


class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
        HashTag.objects.create(tag_name='clothes')
        ShopCategory.objects.create(category_name='salons')
        shop_category = ShopCategory.objects.get(id=1)
        hashtag = HashTag.objects.get(id=1)
        shop_category.allowed_hash_tags.add(hashtag) 
        Day.objects.create(day_name='today')  
        day = Day.objects.get(id=1)        
        ZIPCode.objects.create(District='Kandy', City='Peradeniya', Code='20400')     
        zip_code = ZIPCode.objects.get(id=1)
        shop = Shop.objects.create(user=user, ShopOwner='ShopOwner', ShopName='ShopName', Address='Address',
                             NumOfAds=5, NumOfQuickAds=3, ProfilePic='path', shop_category=shop_category, zip_code=zip_code)
        shop.hash_tags.add(hashtag)
        shop.open_days.add(day)

        customer = Customer.objects.create(user=user, timestamp=datetime.datetime.now())
        customer.followed_shops.add(shop)


    def test_customer_user(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'user')


    def test_customer_timestamp(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('timestamp').verbose_name
        self.assertEquals(field_label, 'timestamp')


# class Follow(models.Model):
#     following = models.ForeignKey(User, related_name="has_followed", on_delete=models.CASCADE)
#     follower = models.ForeignKey(User, related_name="is_followed_by", on_delete=models.CASCADE)
#     follow_time = models.DateTimeField(auto_now=True)

#     def __unicode__(self):
#         return str(self.follow_time)

class FollowModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
       
        user2 = User.objects.create_user(username='john2',
                                 email='jlennon@beatles2.com',
                                 password='glass2 onion')
        follow = Follow.objects.create(following=user1, follower=user2, follow_time=datetime.datetime.now())
        

    def test_follow_following(self):
        follow = Follow.objects.get(id=1)
        field_label = follow._meta.get_field('following').verbose_name
        self.assertEquals(field_label, 'following')


    def test_customer_follower(self):
        follow = Follow.objects.get(id=1)
        field_label = follow._meta.get_field('follower').verbose_name
        self.assertEquals(field_label, 'follower')


    def test_customer_follow_time(self):
        follow = Follow.objects.get(id=1)
        field_label = follow._meta.get_field('follow_time').verbose_name
        self.assertEquals(field_label, 'follow time')



# class Report(models.Model):
#     reporting = models.ForeignKey(User, related_name="has_reported", on_delete=models.CASCADE)
#     reported = models.ForeignKey(User, related_name="is_reported_by", on_delete=models.CASCADE)
#     report_time = models.DateTimeField(auto_now=True)

#     def __unicode__(self):
#         return str(self.report_time)


class ReportModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
       
        user2 = User.objects.create_user(username='john2',
                                 email='jlennon@beatles2.com',
                                 password='glass2 onion')
        report = Report.objects.create(reporting=user1, reported=user2, report_time=datetime.datetime.now())
        

    def test_report_reporting(self):
        report = Report.objects.get(id=1)
        field_label = report._meta.get_field('reporting').verbose_name
        self.assertEquals(field_label, 'reporting')


    def test_customer_reported(self):
        report = Report.objects.get(id=1)
        field_label = report._meta.get_field('reported').verbose_name
        self.assertEquals(field_label, 'reported')


    def test_customer_report_time(self):
        report = Report.objects.get(id=1)
        field_label = report._meta.get_field('report_time').verbose_name
        self.assertEquals(field_label, 'report time')


class DayModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Day.objects.create(day_name='today')

    def test_day(self):
        day = Day.objects.get(id=1)
        field_label = day._meta.get_field('day_name').verbose_name
        self.assertEquals(field_label, 'day name')

    def test_day_name_max_length12(self):
        day = Day.objects.get(id=1)
        max_length = day._meta.get_field('day_name').max_length
        self.assertEquals(max_length, 64)

    def test_object_name_is_day_name10(self):
        day = Day.objects.get(id=1)
        expected_object_name = f'{day.day_name}'
        self.assertEquals(expected_object_name, str(day))

class HashtagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        HashTag.objects.create(tag_name='clothes')

    def test_hash(self):
        hashtag = HashTag.objects.get(id=1)
        field_label = hashtag._meta.get_field('tag_name').verbose_name
        self.assertEquals(field_label, 'tag name')

    def test_hashtag_name_max_length12(self):
        hashtag = HashTag.objects.get(id=1)
        max_length = hashtag._meta.get_field('tag_name').max_length
        self.assertEquals(max_length, 64)
 
    def test_object_name_is_hashtag_name10(self):
        hashtag = HashTag.objects.get(id=1)
        expected_object_name = f'{hashtag.tag_name}'
        self.assertEquals(expected_object_name, str(hashtag))

class ZIPCodeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ZIPCode.objects.create(District='Kandy', City='Peradeniya', Code='20400')

    def test_ZIPCode_District_fieldname(self):
        zipcode = ZIPCode.objects.get(id=1)
        district_fieldname = zipcode._meta.get_field('District').verbose_name
        self.assertEquals(district_fieldname, 'District')

    def test_ZIPCode_City_fieldname(self):
        zipcode = ZIPCode.objects.get(id=1)
        city_fieldname = zipcode._meta.get_field('City').verbose_name
        self.assertEquals(city_fieldname, 'City')

    def test_ZIPCode_Code_fieldname(self):
        zipcode = ZIPCode.objects.get(id=1)
        code_fieldname = zipcode._meta.get_field('Code').verbose_name
        self.assertEquals(code_fieldname, 'Code')

    def test_district_name_max_length12(self):
        zipcode = ZIPCode.objects.get(id=1)
        max_length = zipcode._meta.get_field('District').max_length
        self.assertEquals(max_length, 255)

    def test_city_name_max_length12(self):
        zipcode = ZIPCode.objects.get(id=1)
        max_length = zipcode._meta.get_field('City').max_length
        self.assertEquals(max_length, 255)

    def test_code_name_max_length12(self):
        zipcode = ZIPCode.objects.get(id=1)
        max_length = zipcode._meta.get_field('Code').max_length
        self.assertEquals(max_length, 5)

    def test_object_name_is_district_name(self):
        zipcode = ZIPCode.objects.get(id=1)
        expected_object_name = f'{zipcode.District}'
        self.assertEquals(expected_object_name, str(zipcode.District))

    def test_object_name_is_city_name(self):
        zipcode = ZIPCode.objects.get(id=1)
        expected_object_name = f'{zipcode.City}'
        self.assertEquals(expected_object_name, str(zipcode.City))

    def test_object_name_is_code_name(self):
        zipcode = ZIPCode.objects.get(id=1)
        expected_object_name = f'{zipcode.Code}'
        self.assertEquals(expected_object_name, str(zipcode.Code))



        
class ShopCategoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        HashTag.objects.create(tag_name='clothes')
        
        ShopCategory.objects.create(category_name='salons')
    
    def test_shop_category(self):
        shop_category = ShopCategory.objects.get(id=1)
        field_label = shop_category._meta.get_field('category_name').verbose_name
        self.assertEquals(field_label, 'category name')

    def test_shop_category_manytomany(self):
        shop_category = ShopCategory.objects.get(id=1)
        hashtag = HashTag.objects.get(id=1)
        shop_category.allowed_hash_tags.add(hashtag)
        field_label = shop_category._meta.get_field('allowed_hash_tags').verbose_name
        self.assertEquals(field_label, 'allowed hash tags')


























	