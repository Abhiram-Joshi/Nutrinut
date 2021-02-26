from django import forms
from app.models import UserProfile
from django.contrib.auth.models import User

class UserNamePassForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

        widgets = {

            'username': forms.TextInput(attrs={
                                            'class':'form-control ',
                                            'style':'background-color:#333333; color:white; text-align:center;width: 500px; border-color:#333333',
                                            'required':True,
                                            }),

            'password': forms.PasswordInput(attrs={'class':'form-control ', 'style':'background-color:#333333; color:white; text-align:center; width: 500px; border-color:#333333;'}),

        }


class UserProfileForm(forms.Form):

    mess_choices = (
        ('veg','VEG'),
        ('non-veg','NON-VEG'),
        ('special','SPECIAL'),
    )



    birthdate = forms.DateField(widget = forms.DateInput(attrs={'class':'form-control ', 'style':'background-color:#333333; color:white; text-align:center; width: 500px; border-color:#333333;', 'type':'date'}))


    weight = forms.IntegerField(widget = forms.TextInput(attrs={'class':'form-control ', 'style':'background-color:#333333; color:white; text-align:center; width: 500px; border-color:#333333;'}))


    height = forms.IntegerField(widget = forms.TextInput(attrs={'class':'form-control ', 'style':'background-color:#333333; color:white; text-align:center; width: 500px; border-color:#333333;'}))





class DayMealForm(forms.Form):
    day_choices = (
        ('monday','Monday'),
        ('tuesday','Tudesday'),
        ('wednesday','Wednesday'),
        ('thursday','Thursday'),
        ('friday','Friday'),
        ('saturday','Saturday'),
        ('sunday','Sunday'),
    )

    day = forms.CharField(
        label = "Day",
        widget = forms.RadioSelect(choices = day_choices),
    )


    meal_choices = (
        ('breakfast','Breakfast'),
        ('lunch','Lunch'),
        ('dinner','Dinner'),
    )

    meal = forms.CharField(
        label = "Meal",
        widget = forms.RadioSelect(choices = meal_choices),
    )



#Mess Food Forms
class BFoodForm(forms.Form):

    items = (
        ('aloo_paratha','Aloo Paratha'),
        ('bread','Bread'),
        ('coffee','Coffee'),
        ('cornflakes','Cornflakes'),
        ('egg','Egg'),
        ('gobi_paratha','Gobi Paratha'),
        ('idli','Idli'),
        ('masala_dosa','Masala Dosa'),
        ('milk','Milk'),
        ('omelete','Omelete'),
        ('orange_juice','Orange Juice'),
        ('pav_bhaji','Pav Bhaji'),
        ('poha','Poha'),
        ('samosa','Samosa'),
        ('sewai','Sewai'),
        ('strawberry_juice','Strawberry Juice'),
        ('tea','Tea'),
        ('upma','Upma'),
        ('uttapam','Uttapam'),
        ('vada_pav','Vada Pav'),
    )

    food = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        choices = items,
    )

    # widgets = {
    #     'food': forms.CheckboxSelectMultiple(attrs={
    #                                             'style' : 'font-family: dm sans; font-size:20px;'
    #                                         })
    # }


class LFoodForm(forms.Form):

    items = (
        ('aloo_capsicum','Aloo Capsicum'),
        ('aloo_jeera','Aloo Jeera'),
        ('bhindi','Bhindi'),
        ('brinjal','Brinjal'),
        ('carrot_sabzi','Carrot Sabzi'),
        ('chana_dal','Chana Dal'),
        ('chicken_biriyani','Chicken Biriyani'),
        ('dal_fry','Dal Fry'),
        ('dal_maharani','Dal Maharani'),
        ('dal_makhani','Dal Makhani'),
        ('dal_rajasthani','Dal Rajasthani'),
        ('kadhai_veg','Kadhai Veg'),
        ('kadi','Kadi'),
        ('onion_raita','Onion Raita'),
        ('paneer','Paneer'),
        ('potato_chips','Potato Chips'),
        ('rasam','Rasam'),
        ('rice','Rice'),
        ('roti','Roti'),
        ('sambhar','Sambar'),
    )

    food = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        choices = items,
    )


class DFoodForm(forms.Form):

    items = (
        ('baby_corn','Baby Corn'),
        ('bisbelle_bath','Bisbelle Bath'),
        ('bhindi','Bhindi'),
        ('cabbage','Cabbage'),
        ('chana_masala','Chana Masala'),
        ('chicken_masala','Chicken Masala'),
        ('chowmein','Chowmein'),
        ('dal_punjabi','Dal Punjabi'),
        ('dal_tadka','Dal Tadka'),
        ('dam_aloo','Dam Aloo'),
        ('gajar_ka_halwa','Gajar ka Halwa'),
        ('jeera_pulao','Jeera Pulao'),
        ('jeera_rice','Jeera Rice'),
        ('kaala_dal_fry','Kaala Dal Fry'),
        ('peas_pulao','Peas Pulao'),
        ('puri','Puri'),
        ('sambhar','Sambar'),
        ('soup','Soup'),
        ('uttapam','Uttapam'),
        ('veg_korma','Veg Korma'),
    )

    food = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        choices = items,
    )





#Restaurant Food Forms
class RBFoodForm(forms.Form):

    items = (
        ('aloo_paratha','Aloo Paratha'),
        ('bread','Bread'),
        ('coffee','Coffee'),
        ('cornflakes','Cornflakes'),
        ('egg','Egg'),
        ('gobi_paratha','Gobi Paratha'),
        ('idli','Idli'),
        ('masala_dosa','Masala Dosa'),
        ('milk','Milk'),
        ('omelete','Omelete'),
        ('orange_juice','Orange Juice'),
        ('pav_bhaji','Pav Bhaji'),
        ('poha','Poha'),
        ('samosa','Samosa'),
        ('sewai','Sewai'),
        ('strawberry_juice','Strawberry Juice'),
        ('tea','Tea'),
        ('upma','Upma'),
        ('uttapam','Uttapam'),
        ('vada_pav','Vada Pav'),
    )

    food = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        choices = items,
    )


class RLFoodForm(forms.Form):

    items = (
        ('aloo_capsicum','Aloo Capsicum'),
        ('aloo_jeera','Aloo Jeera'),
        ('bhindi','Bhindi'),
        ('brinjal','Brinjal'),
        ('carrot_sabzi','Carrot Sabzi'),
        ('chana_dal','Chana Dal'),
        ('chicken_biriyani','Chicken Biriyani'),
        ('dal_fry','Dal Fry'),
        ('dal_maharani','Dal Maharani'),
        ('dal_makhani','Dal Makhani'),
        ('dal_rajasthani','Dal Rajasthani'),
        ('kadhai_veg','Kadhai Veg'),
        ('kadi','Kadi'),
        ('onion_raita','Onion Raita'),
        ('paneer','Paneer'),
        ('potato_chips','Potato Chips'),
        ('rasam','Rasam'),
        ('rice','Rice'),
        ('roti','Roti'),
        ('sambhar','Sambar'),
    )

    food = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        choices = items,
    )


class RDFoodForm(forms.Form):

    items = (
        ('baby_corn','Baby Corn'),
        ('bisbelle_bath','Bisbelle Bath'),
        ('bhindi','Bhindi'),
        ('cabbage','Cabbage'),
        ('chana_masala','Chana Masala'),
        ('chicken_masala','Chicken Masala'),
        ('chowmein','Chowmein'),
        ('dal_punjabi','Dal Punjabi'),
        ('dal_tadka','Dal Tadka'),
        ('dam_aloo','Dam Aloo'),
        ('gajar_ka_halwa','Gajar ka Halwa'),
        ('jeera_pulao','Jeera Pulao'),
        ('jeera_rice','Jeera Rice'),
        ('kaala_dal_fry','Kaala Dal Fry'),
        ('peas_pulao','Peas Pulao'),
        ('puri','Puri'),
        ('sambhar','Sambar'),
        ('soup','Soup'),
        ('uttapam','Uttapam'),
        ('veg_korma','Veg Korma'),
    )

    food = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        choices = items,
    )
