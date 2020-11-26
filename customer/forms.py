from django import forms
from django.utils import timezone
from customer.models import customer
from customer.models import Questionaire

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ("name", "email", "date", "comment",  )   # NOTE: the trailing comma is required
        

class QuestionaireForm(forms.ModelForm):
    class Meta:
        model = Questionaire
        fields = ("name", "email", "date", "dob", "gender", "medicaldignosis","medicaldignosisdate","location", 
        "Q_1_When_Im_walking_I_deliberately_notice_the_sensations_of_my_body_moving","Q_2_Im_good_at_finding_words_to_describe_my_feelings",
        "Q_3_I_criticise_myself_for_having_irrational_or_inappropriate_emotions","Q_4_I_perceive_my_feelings_and_emotions_without_having_to_react_to_them",
        "Q_5_When_I_do_things_my_mind_wanders_off_and_Im_easily_distracted","Q_6_When_I_take_a_shower_or_bath_I_stay_alert_to_the_sensations_of_water_on_my_body",
        "Q_7_I_can_easily_put_my_beliefs_opinions_and_expectations_into_words","Q_8_I_dont_pay_attention_to_what_Im_doing_because_Im_daydreaming_worrying_or_otherwise_distracted",
        "Q_9_I_watch_my_feelings_without_getting_lost_in_them","Q_10_I_tell_myself_I_shouldnt_be_feeling_the_way_Im_feeling",
        "Q_11_I_notice_how_foods_and_drinks_affect_my_thoughts_bodily_sensations_and_emotions","Q_12_Its_hard_for_me_to_find_the_words_to_describe_what_Im_thinking",
        "Q_13_I_am_easily_distracted","Q_14_I_believe_some_of_my_thoughts_are_abnormal_or_bad_and_I_shouldnt_think_that_way",
        "Q_15_I_pay_attention_to_sensations_such_as_the_wind_in_my_hair_or_sun_on_my_face","Q_16_I_have_trouble_thinking_of_the_right_words_to_express_how_I_feel_about_things",
        "Q_17_I_make_judgments_about_whether_my_thoughts_are_good_or_bad","Q_18_I_find_it_difficult_to_stay_focused_on_whats_happening_in_the_present",
        "Q_19_When_I_have_distressing_thoughts_or_images_I_step_back_and_am_aware_of_the_thought_or_image_without_getting_taken_over_by_it",
        "Q_20_I_pay_attention_to_sounds_such_as_clocks_ticking_birds_chirping_or_cars_passing","Q_21_In_difficult_situations_I_can_pause_without_immediately_reacting",
        "Q_22_When_I_have_a_sensation_in_my_body_its_difficult_for_me_to_describe_it_because_I_cant_find_the_right_words","Q_23_It_seems_I_am_running_on_automatic_without_much_awareness_of_what_Im_doing",
        "Q_24_When_I_have_distressing_thoughts_or_images_I_feel_calm_soon_after","Q_25_I_tell_myself_thatI_shouldnt_be_thinking_the_way_Im_thinking","Q_26_I_notice_the_smells_and_aromas_of_things","Q_27_Even_when_Im_feeling_terribly_upset_I_can_find_a_way_to_put_it_into_words",
        "Q_28_I_rush_through_activities_without_being_really_attentive_to_them","Q_29_When_I_have_distressing_thoughts_or_images_I_am_able_just_to_notice_them_without_reacting","Q_30_I_think_some_of_my_emotions_are_bad_or_inappropriate_and_I_shouldnt_feel_them",
        "Q_31_I_notice_visual_elements_in_art_or_nature_such_as_colours_shapes_textures_or_patterns_of_light_and_shadow","Q_32_My_natural_tendency_is_to_put_my_experiences_into_words","Q_33_When_I_have_distressing_thoughts_or_images_I_just_notice_them_and_let_them_go",
        "Q_34_I_do_jobs_or_tasks_automatically_without_being_aware_of_what_Im_doing","Q_35_When_I_have_distressing_thoughts_or_images_I_judge_myself_as_good_or_bad_depending_what_the_thought_or_image_is_about",
        "Q_36_I_pay_attention_to_how_my_emotions_affect_my_thoughts_and_behaviour","Q_37_I_can_usually_describe_how_I_feel_at_the_moment_in_considerable_detail",
        "Q_38_I_find_myself_doing_things_without_paying_attention","Q_39_I_disapprove_of_myself_when_I_have_irrational_ideas",)