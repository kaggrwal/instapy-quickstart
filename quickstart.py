""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'secluded_nomad'
insta_password = 'Infinity@314'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username, password=insta_password, bypass_suspicious_attempt=True,headless_browser=False)
unfollow_whitelist=['somyarora96'
'lovephrases'
'kaniikagoel'
'pallavisingh2021'
'48lawsoflove'
'astha.shukla16'
'anjali_jassal'
'justinsandersofficial'
'crazy.lyricist'
'vasu084'
'manvirelia'
'heavens_concept'
'_richa_98'
'itspriyanshasingh'
'_teja_vu_'
'wild_islandboy04'
'roy_50m'
'rachanaswamy'
'poojachaudhary_preet_'
'rituverma42'
'kimkeepup'
'daily.1.thing'
'navedits_'
'stargateobservatory'
'_tanya._.sharma_'
'intimidatingillusions'
'sumansher'
'pheasyque'
'kavishala.in'
'shanayasharma95'
'unpluggedgurgaon'
'darkpoetesss'
'surajgarhgurgaon'
'nabypal'
'official.diary_ticko'
'real._.is._.rare._'
'astrobackyard'
'andykennedy_photos'
'musings_of_existence'
'bollywoodgandu'
'betweenlettersandlines'
'_isavage_'
'superhumour'
'_adultgram_'
'shreyasingh__4'
'log.kis.kisko.thokenge'
'desi_idiot'
'cherubb_'
'e_tirado'
'itsonlywordsofficial'
'naruto.otakus'
'shriya_mj'
'theminimalist_india'
'_wildsecrets_'
'poojaprajapati93192248'
'dharamshalalocal'
'the_indian_web_series'
'_classyapparels_'
'inrishikesh'
'nehashah022292'
'wander.on'
'bombaytrooper'
'desi.joke'
'yogaholick'
'kolkatasillusion_official'
'moxtain_community'
'jammutourism'
'eyesofaleshee'
'rasmandeep'
'shreya_j01'
'nit_art01'
'ayushmannk'
'hire_tale'
'the_travelling_hermit'
'royalenfield'
'p.s_lifestylez'
'night_shoot_out'
'moto_bankerr'
'deekshatiwari9'
'shiny_collection12'
'mrbeanbagg'
'movieshowss'
'deepanshu_1995'
'priyasweet.sansanwal'
'people_who_rise'
'apextvofficial'
'dlf_cyberhub'
'latest_one.in'
'trendfilms'
'ixigo'
'artistsadda'
'oneplus'
'thelocaltrain'
'kailash.kumar11'
'famehazel'
'sassy_thoughts'
'onlyfullfacts'
'6amsuccess'
'gahlotbaba'
'adventure_nation_outdoor_tribe'
'kriti.kharbanda'
'akaushal2945'
'time4knowledge'
'codechef'
'usabilla'
'gopaldatt'
'shootguru'
'wandering_dreamcatcher'
'swati.k09'
'workoutsofficial'
'monkey__shanti'
'mrwhosetheboss'
'traveler_pnkz'
'lalitshokeen1515'
'horrorphiles'
'fairwarningcareers'
'vision_of_india'
'sumeetvyas'
'exploring_through_lens'
'dpeginsta'
'photographers_hub_india'
'igersofindia'
'travelrealindia'
'indiapictures'
'yourshot_india'
'click_india_click'
'india.clicks'
'indian.photography'
'streetphotographyindia'
'dslrofficial'
'alishaa__kapoor'
'singh_nikita'
'tiadey20'
'appy_appuz'
'roycebairphoto'
'scrawledstories'
'wevolverapp'
'nerd.cast'
'monikaspeaks'
'captured_insta'
'millionaire_scheduling_'
'developerjobs4you'
'thehubblescope'
'virtuality'
'ethereal.colours'
'futurism'
'curiositydotcom'
'chemistryjokes'
'sciencejoke.s'
'yusuf_firoz287'
'troll_punjabi'
'massimorinaldi27'
'simrankaur9492'
'thephotonut'
'desi_diaries'
'8.visual'
'nikonindiaofficial'
'colours.of.india'
'bnw_india'
'spacex'
'rajography'
'photoddiction'
'jitendrak1'
'indiatravelgram'
'indianshutterbugs'
'stories.of.india'
'delhigram'
'rahul623ee'
'virat.kohli'
'sidjaggi92'
'the.ramukaka'
'humansofchandigarh'
'500px'
'streets.of.india'
'dil.di.gal'
'akshaykumar'
'namelesspc'
'gaurav3237'
'the.realshit.gyan'
'historytv18'
'narendramodi'
'allindiabakchod'
'monikarawat10'
'codingblog'
'tvfqtiyapa'
'asapscience'
'factbolt'
'chandigarhians__'
'theawkwardyeti'
'prachidesai'
'pu_chd'
'barked'
'thegoodquote'
'sarcasm_only'
'evelyn_sharma'
'nina'
'naruto'
'jacquelinef143'
'ileana_official'
'himanshu2992'
'priyankachopra'
'aliaabhatt'
'deepikapadukone'
'natgeo'
'selenagomez'
'instagram'
'harjotsinghphotography'
'9gag'
'unheard_shayri'
'villainquote'
'photowalkdelhi'
'stereoindia'
'sakshimalik'
'thescientistfacts'
'technicalbaba_'
'corporate.bytes'
'divinebucketlist'
'ode_to_travel'
'asabhyak'
'chan.singh7'
'navagg79'
'namelsspc'
'photgraphers_of_india'
'yourstory_co'
'hiswriteups'
'longexpo_shotz'
'geekspin'
'elonmusk'
'thescribbledstories'
'ttt_official'
'scoopwhoop'
'thewashroomstories'
'amandacerny'
'ishivyas18'
'garbagebinofficial'
'bosplanet'
'theunrulytravler'
'sosfashion75'
'innervoicewf'
'zostel'
'getpoliticl'
'linkedinlife'
'google'
'taranjit.kaur20'
'bae_video_picture'
'watch_world_0005'
'originalindia_',
'bnw_india']
tag_blacklist=['#porn', '#sex', '#hotgirl', '#instaporn', '#deals', '#sexy', '#likeforlike', '#followforfollow', '#hot',
                   '#breakup', '#urdu', '#love', '#tiktok', '#musically']

tag_list=['wanderlust', '_soi', 'nikonindia', 'bnwphotography', 'incredibleindia', 'travelislife',
              'photographers_of_india', 'travelgram', 'storiesofindia', '_woi', 'visionofpictures', 'shots_of_india',
              'newphotographers', 'instawriters', 'writersofindia', 'igwriters', 'poetry','yourquote', 'instawriters',
              'writersofinstagram', 'writersofindia', 'quoteoftheday', 'astrophotgraphy','universe',]



with smart_run(session):
    """ Activity flow """
    # general settings

    session.set_relationship_bounds(enabled=True,
				 potency_ratio=0.64,
				  delimit_by_numbers=True,
				   max_followers=85000,
				    max_following=4490,
				     min_followers=100,
				      min_following=16,
				       min_posts=10,
                max_posts=10000)


    session.set_quota_supervisor(enabled=True, sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes=(37, 585),
                               peak_comments=(None, None),
                                peak_follows=(10,100),
                                 peak_unfollows=(5, 70),
                                  peak_server_calls=(None, 4700))



    session.set_skip_users(skip_private=False,
                       skip_no_profile_pic=True,
                       no_profile_pic_percentage=100)

    session.set_dont_include(unfollow_whitelist)

    session.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
    session.set_do_follow(enabled=True, percentage=70, times=1)
    session.set_do_like(enabled=True, percentage=70)
    session.set_dont_unfollow_active_users(enabled=True, posts=3)
    session.set_dont_like(tag_blacklist)

    session.follow_by_tags(tag_list, amount=10)
    session.like_by_tags(tag_list, amount=10)
    session.like_by_feed(amount=1, randomize=True, unfollow=True, interact=True)
    #session.interact_user_following(tag_list, amount=10, randomize=True)
    session.unfollow_users(amount=10, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)




 
