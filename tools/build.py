"""Furog Games sitesini üretir (statik HTML). Çalıştır: python3 tools/build.py
Sayfalar: / (+/tr/) ve her oyun için /<oyun>/ (+tr) · /<oyun>/privacy/ (+tr) · /<oyun>/support/ (+tr)
Oyunlar GAMES listesinde; iletişim e-postası ve App Store bağlantıları aşağıdaki sabitlerde.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTACT_EMAIL = "marinariogroup@gmail.com"      # yayımlanacak destek e-postası

# Ortak arayüz metinleri
T = {
    "en": {
        "lang": "en", "other": "tr", "other_name": "Türkçe",
        "store": "Download on the App Store", "soon": "Coming soon to the App Store",
        "features_title": "What you do",
        "privacy": "Privacy Policy", "support": "Support",
        "home_desc": "We make small, cozy games.",
        "footer": "© 2026 Furog Games",
    },
    "tr": {
        "lang": "tr", "other": "en", "other_name": "English",
        "store": "App Store'dan indir", "soon": "Yakında App Store'da",
        "features_title": "Oyunda neler var",
        "privacy": "Gizlilik Politikası", "support": "Destek",
        "home_desc": "Küçük, sıcak oyunlar yapıyoruz.",
        "footer": "© 2026 Furog Games",
    },
}

# ---------------------------------------------------------------- Tiny Couriers

TC_EFFECTIVE = {"en": "November 16, 2026", "tr": "16 Kasım 2026"}

TINY_COURIERS = {
    "slug": "tiny-couriers",
    "name": "Tiny Couriers",
    "app_store_url": "",                  # yayına çıkınca: https://apps.apple.com/app/idXXXXXXXXX
    "icon": "tiny-couriers-icon.png",
    "shots": ["shot-play.jpg", "shot-orders.jpg", "shot-upgrades.jpg", "shot-island.jpg"],  # iki dilde aynı
    "text": {
        "en": {
            "tagline": "Run a tiny delivery company on a floating sky-island city.",
            "lead": "Take orders from burger joints, bakeries and flower shops, send your couriers zipping "
                    "across town on their scooters, collect the coins and grow your fleet — district by district.",
            "features": [
                ("Dispatch orders", "Pick the right courier for every order before it runs out of time."),
                ("Grow your fleet", "Hire couriers, sign contracts with local shops and unlock new districts."),
                ("Upgrade everything", "Faster scooters, more orders, auto-collect and a manager who works while you're away."),
                ("Pause and plan", "Freeze the map, assign everyone, then hit play and watch them go."),
            ],
        },
        "tr": {
            "tagline": "Gökyüzünde yüzen bir ada şehrinde minik bir kurye şirketi yönet.",
            "lead": "Burgerciden, fırından, çiçekçiden gelen siparişleri al; kuryelerini scooter'larıyla şehrin "
                    "dört bir yanına gönder, paraları topla ve filonu mahalle mahalle büyüt.",
            "features": [
                ("Siparişleri dağıt", "Her siparişi süresi dolmadan doğru kuryeye ata."),
                ("Filonu büyüt", "Kurye al, dükkânlarla sözleşme imzala, yeni mahalleler aç."),
                ("Her şeyi geliştir", "Hızlı scooterlar, daha çok sipariş, otomatik toplama ve sen yokken çalışan bir müdür."),
                ("Durdur ve planla", "Haritayı dondur, herkesi ata, sonra oynat ve kuryelerini izle."),
            ],
        },
    },
    "privacy": {
        "en": f"""
<h1>Privacy Policy — Tiny Couriers</h1>
<p class="meta">Effective date: {TC_EFFECTIVE['en']} · Developer: Furog Games</p>
<p>This policy explains what information the game <b>Tiny Couriers</b> ("the app") handles. In short: the game
itself does not collect personal data and has no accounts. It shows optional rewarded ads through Google AdMob,
and Google may collect some device data to serve those ads.</p>

<h2>1. Data the game stores</h2>
<p>Your progress (money, couriers, upgrades, settings such as music volume and language) is saved
<b>only on your device</b>. We do not run servers, we do not have user accounts, and this data is never sent to us.
Deleting the app deletes this data.</p>

<h2>2. Advertising (Google AdMob)</h2>
<p>The app can show an <b>optional rewarded video ad</b> (for example to double your offline earnings). Ads are
provided by Google AdMob. To show and measure ads, Google's Mobile Ads SDK may collect:</p>
<ul>
  <li>Device identifiers — the Identifier for Advertisers (IDFA) <b>only if you allow tracking</b> in the iOS
      "Allow app to track" prompt;</li>
  <li>approximate location derived from your IP address;</li>
  <li>device information (model, operating system, language) and interactions with ads;</li>
  <li>diagnostic data such as crashes and performance.</li>
</ul>
<p>If you do not allow tracking, ads are still shown but are not personalized with the IDFA. You can change this any
time in iOS Settings → Privacy &amp; Security → Tracking. Google's use of this data is described in
<a href="https://policies.google.com/privacy">Google's Privacy Policy</a> and
<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its services</a>.</p>

<h2>3. Children</h2>
<p>The app is not directed at children under 13, and we do not knowingly collect personal information from
children. Ads are limited to content suitable for general audiences.</p>

<h2>4. Your rights</h2>
<p>Because we do not hold any of your personal data, there is nothing for us to access, correct or delete on our
side. For data processed by Google for advertising, use the controls described in Google's policies, or reset
your advertising identifier in iOS settings.</p>

<h2>5. Changes</h2>
<p>If this policy changes, we will update this page and the effective date above.</p>

<h2>6. Contact</h2>
<p>Questions about privacy: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
""",
        "tr": f"""
<h1>Gizlilik Politikası — Tiny Couriers</h1>
<p class="meta">Yürürlük tarihi: {TC_EFFECTIVE['tr']} · Geliştirici: Furog Games</p>
<p>Bu politika, <b>Tiny Couriers</b> oyununun ("uygulama") hangi bilgileri işlediğini açıklar. Kısaca: oyunun
kendisi kişisel veri toplamaz ve hesap sistemi yoktur. İsteğe bağlı ödüllü reklamlar Google AdMob üzerinden
gösterilir; Google bu reklamları sunmak için bazı cihaz verilerini toplayabilir.</p>

<h2>1. Oyunun sakladığı veriler</h2>
<p>İlerlemen (para, kuryeler, geliştirmeler, müzik seviyesi ve dil gibi ayarlar) <b>sadece cihazında</b> saklanır.
Sunucumuz ve kullanıcı hesabı yoktur; bu veriler bize hiçbir zaman gönderilmez. Uygulamayı silmek bu verileri de
siler.</p>

<h2>2. Reklamlar (Google AdMob)</h2>
<p>Uygulama <b>isteğe bağlı ödüllü video reklam</b> gösterebilir (ör. sen yokken kazandığın parayı ikiye katlamak
için). Reklamlar Google AdMob tarafından sağlanır. Reklamları göstermek ve ölçmek için Google'ın Mobile Ads SDK'sı
şunları toplayabilir:</p>
<ul>
  <li>Cihaz tanımlayıcıları — Reklam Tanımlayıcısı (IDFA), <b>sadece iOS'un "Uygulamanın izlemesine izin ver"
      sorusuna izin verirsen</b>;</li>
  <li>IP adresinden çıkarılan yaklaşık konum;</li>
  <li>cihaz bilgileri (model, işletim sistemi, dil) ve reklamlarla etkileşimler;</li>
  <li>çökme ve performans gibi tanılama verileri.</li>
</ul>
<p>İzlemeye izin vermezsen reklamlar yine gösterilir ama IDFA ile kişiselleştirilmez. Bunu istediğin zaman
iOS Ayarlar → Gizlilik ve Güvenlik → İzleme bölümünden değiştirebilirsin. Google'ın bu verileri nasıl kullandığı
<a href="https://policies.google.com/privacy?hl=tr">Google Gizlilik Politikası</a>'nda ve
<a href="https://policies.google.com/technologies/partner-sites?hl=tr">Google'ın, hizmetlerini kullanan sitelerden ve uygulamalardan gelen bilgileri nasıl kullandığı</a> sayfasında açıklanır.</p>

<h2>3. Çocuklar</h2>
<p>Uygulama 13 yaş altındaki çocuklara yönelik değildir ve çocuklardan bilerek kişisel bilgi toplamayız. Reklamlar
genel izleyiciye uygun içerikle sınırlıdır.</p>

<h2>4. Hakların</h2>
<p>Kişisel verilerinden hiçbirini tutmadığımız için bizim tarafımızda erişilecek, düzeltilecek ya da silinecek bir
veri yoktur. Google'ın reklam için işlediği veriler için Google'ın politikalarındaki ayarları kullanabilir ya da
iOS ayarlarından reklam tanımlayıcını sıfırlayabilirsin. 6698 sayılı KVKK kapsamındaki başvuruların için aşağıdaki
adresten bize ulaşabilirsin.</p>

<h2>5. Değişiklikler</h2>
<p>Bu politika değişirse bu sayfayı ve yukarıdaki yürürlük tarihini güncelleriz.</p>

<h2>6. İletişim</h2>
<p>Gizlilikle ilgili sorular: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
""",
    },
    "support": {
        "en": f"""
<h1>Tiny Couriers — Support</h1>
<p>Found a bug, have an idea, or need help? Write to us at
<a href="mailto:{CONTACT_EMAIL}?subject=Tiny%20Couriers">{CONTACT_EMAIL}</a>. Please include your iPhone model and iOS
version, and a screenshot if you can. We usually reply within a few days.</p>
<h2>Frequently asked</h2>
<h3>Where is my progress saved?</h3>
<p>On your device. If you delete the app, your progress is deleted too.</p>
<h3>How do I turn off music or sounds, or change the language?</h3>
<p>Tap the gear button at the top right. Music, sound effects, music volume and language are all there.</p>
<h3>How does the manager work?</h3>
<p>Hire a manager in the Staff panel. While the game is closed, the manager keeps delivering orders and you collect
the earnings when you come back.</p>
<h3>Can I stop the game to plan?</h3>
<p>Yes. The pause button next to the gear freezes the map: you can still open menus, collect coins and assign
orders. Press play to continue.</p>
<h3>Do I have to watch ads?</h3>
<p>No. Ads are optional; they only appear when you choose to double your offline earnings.</p>
""",
        "tr": f"""
<h1>Tiny Couriers — Destek</h1>
<p>Bir hata mı buldun, bir fikrin mi var ya da yardım mı lazım? Bize
<a href="mailto:{CONTACT_EMAIL}?subject=Tiny%20Couriers">{CONTACT_EMAIL}</a> adresinden yaz. Lütfen iPhone modelini ve iOS
sürümünü, mümkünse bir ekran görüntüsü ekle. Genelde birkaç gün içinde dönüyoruz.</p>
<h2>Sık sorulanlar</h2>
<h3>İlerlemem nerede saklanıyor?</h3>
<p>Cihazında. Uygulamayı silersen ilerlemen de silinir.</p>
<h3>Müziği ya da sesleri nasıl kapatırım, dili nasıl değiştiririm?</h3>
<p>Sağ üstteki dişli butonuna dokun. Müzik, ses efektleri, müzik seviyesi ve dil orada.</p>
<h3>Müdür nasıl çalışır?</h3>
<p>Personel panelinden müdür al. Oyun kapalıyken müdür siparişleri teslim etmeye devam eder, geri döndüğünde
kazancı toplarsın.</p>
<h3>Plan yapmak için oyunu durdurabilir miyim?</h3>
<p>Evet. Dişlinin yanındaki duraklat butonu haritayı dondurur: menüleri açabilir, para toplayabilir ve sipariş
atayabilirsin. Devam etmek için oynata bas.</p>
<h3>Reklam izlemek zorunda mıyım?</h3>
<p>Hayır. Reklamlar isteğe bağlı; sadece çevrimdışı kazancını ikiye katlamayı seçtiğinde çıkar.</p>
""",
    },
}

# ---------------------------------------------------------------- Marble Mosaic

MM_EFFECTIVE = {"en": "November 25, 2026", "tr": "25 Kasım 2026"}

MARBLE_MOSAIC = {
    "slug": "marble-mosaic",
    "name": "Marble Mosaic",
    "app_store_url": "",                  # yayına çıkınca: https://apps.apple.com/app/idXXXXXXXXX
    "icon": "marble-mosaic-icon.png",
    "shots": ["mm-shot-play-{lang}.jpg", "mm-shot-levels-{lang}.jpg", "mm-shot-hidden-{lang}.jpg", "mm-shot-ice-{lang}.jpg"],
    "text": {
        "en": {
            "tagline": "A relaxing marble-sorting puzzle where every level is a picture.",
            "lead": "Tap the trays, watch the marbles roll through the funnel into cups of the same color, "
                    "and clear the board to complete the picture.",
            "features": [
                ("Sort by color", "Every marble rolls into the cup of its own color. Plan your taps so the funnel never overflows."),
                ("150+ pictures", "Strawberries, castles, rockets and more, with new levels on the way."),
                ("Fresh twists", "Mystery trays hide their color until you reach them, and frozen trays melt as you play."),
                ("Boosters and daily rewards", "Undo a move, widen the funnel with +2 Funnel and collect coins every day."),
            ],
        },
        "tr": {
            "tagline": "Her seviyesi bir resim olan rahatlatıcı bir bilye ayırma bulmacası.",
            "lead": "Tepsilere dokun, bilyeler huniden yuvarlanıp aynı renkteki bardaklara düşsün; "
                    "tahtayı temizle, resmi tamamla.",
            "features": [
                ("Renklerine göre ayır", "Her bilye kendi rengindeki bardağa yuvarlanır. Huni taşmasın diye hamlelerini planla."),
                ("150+ resim", "Çilekler, kaleler, roketler ve daha fazlası; yeni seviyeler de yolda."),
                ("Yeni sürprizler", "Gizli tepsiler sen ulaşana kadar rengini saklar, buzlu tepsiler oynadıkça erir."),
                ("Güçlendiriciler ve günlük ödül", "Hamleni geri al, +2 Huni ile huniyi genişlet, her gün altın topla."),
            ],
        },
    },
    "privacy": {
        "en": f"""
<h1>Privacy Policy — Marble Mosaic</h1>
<p class="meta">Effective date: {MM_EFFECTIVE['en']} · Developer: Furog Games</p>
<p>This policy explains what information the game <b>Marble Mosaic</b> ("the app") handles. In short: the game
itself does not collect personal data and has no accounts. It shows ads through Google AdMob, and Google may
collect some device data to serve those ads.</p>

<h2>1. Data the game stores</h2>
<p>Your progress (completed levels, best moves, coins, daily reward streak and settings such as music volume,
vibration and language) is saved <b>only on your device</b>. We do not run servers, we do not have user accounts,
and this data is never sent to us. Deleting the app deletes this data.</p>

<h2>2. Advertising (Google AdMob)</h2>
<p>The app shows two kinds of ads, provided by Google AdMob:</p>
<ul>
  <li><b>optional rewarded video ads</b>, only when you choose to watch one (for example to double your coins,
      to get +2 funnel space or an extra undo);</li>
  <li><b>short full-screen ads between levels</b>, shown from time to time after you finish or retry a level.</li>
</ul>
<p>To show and measure ads, Google's Mobile Ads SDK may collect:</p>
<ul>
  <li>Device identifiers — the Identifier for Advertisers (IDFA) <b>only if you allow tracking</b> in the iOS
      "Allow app to track" prompt;</li>
  <li>approximate location derived from your IP address;</li>
  <li>device information (model, operating system, language) and interactions with ads;</li>
  <li>diagnostic data such as crashes and performance.</li>
</ul>
<p>If you are in the European Economic Area, the United Kingdom or Switzerland, the app asks for your consent
through Google's consent form before ads are personalized. If you do not allow tracking, ads are still shown but are
not personalized with the IDFA. You can change this any time in iOS Settings → Privacy &amp; Security → Tracking.
Google's use of this data is described in
<a href="https://policies.google.com/privacy">Google's Privacy Policy</a> and
<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its services</a>.</p>

<h2>3. Children</h2>
<p>The app is not directed at children under 13, and we do not knowingly collect personal information from
children. Ads are limited to content suitable for general audiences.</p>

<h2>4. Your rights</h2>
<p>Because we do not hold any of your personal data, there is nothing for us to access, correct or delete on our
side. For data processed by Google for advertising, use the controls described in Google's policies, or reset
your advertising identifier in iOS settings.</p>

<h2>5. Changes</h2>
<p>If this policy changes, we will update this page and the effective date above.</p>

<h2>6. Contact</h2>
<p>Questions about privacy: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
""",
        "tr": f"""
<h1>Gizlilik Politikası — Marble Mosaic</h1>
<p class="meta">Yürürlük tarihi: {MM_EFFECTIVE['tr']} · Geliştirici: Furog Games</p>
<p>Bu politika, <b>Marble Mosaic</b> oyununun ("uygulama") hangi bilgileri işlediğini açıklar. Kısaca: oyunun
kendisi kişisel veri toplamaz ve hesap sistemi yoktur. Reklamlar Google AdMob üzerinden gösterilir; Google bu
reklamları sunmak için bazı cihaz verilerini toplayabilir.</p>

<h2>1. Oyunun sakladığı veriler</h2>
<p>İlerlemen (tamamlanan seviyeler, en iyi hamleler, altın, günlük ödül serisi ve müzik seviyesi, titreşim, dil gibi
ayarlar) <b>sadece cihazında</b> saklanır. Sunucumuz ve kullanıcı hesabı yoktur; bu veriler bize hiçbir zaman
gönderilmez. Uygulamayı silmek bu verileri de siler.</p>

<h2>2. Reklamlar (Google AdMob)</h2>
<p>Uygulama Google AdMob tarafından sağlanan iki tür reklam gösterir:</p>
<ul>
  <li><b>isteğe bağlı ödüllü video reklamlar</b>, sadece sen izlemeyi seçtiğinde (ör. altınını ikiye katlamak,
      +2 huni yeri ya da ekstra geri alma hakkı kazanmak için);</li>
  <li><b>seviyeler arasında kısa tam ekran reklamlar</b>, bir seviyeyi bitirdikten ya da yeniden denedikten sonra
      zaman zaman gösterilir.</li>
</ul>
<p>Reklamları göstermek ve ölçmek için Google'ın Mobile Ads SDK'sı şunları toplayabilir:</p>
<ul>
  <li>Cihaz tanımlayıcıları — Reklam Tanımlayıcısı (IDFA), <b>sadece iOS'un "Uygulamanın izlemesine izin ver"
      sorusuna izin verirsen</b>;</li>
  <li>IP adresinden çıkarılan yaklaşık konum;</li>
  <li>cihaz bilgileri (model, işletim sistemi, dil) ve reklamlarla etkileşimler;</li>
  <li>çökme ve performans gibi tanılama verileri.</li>
</ul>
<p>Avrupa Ekonomik Alanı, Birleşik Krallık ya da İsviçre'deysen uygulama, reklamlar kişiselleştirilmeden önce
Google'ın onay formuyla iznini ister. İzlemeye izin vermezsen reklamlar yine gösterilir ama IDFA ile
kişiselleştirilmez. Bunu istediğin zaman iOS Ayarlar → Gizlilik ve Güvenlik → İzleme bölümünden değiştirebilirsin.
Google'ın bu verileri nasıl kullandığı
<a href="https://policies.google.com/privacy?hl=tr">Google Gizlilik Politikası</a>'nda ve
<a href="https://policies.google.com/technologies/partner-sites?hl=tr">Google'ın, hizmetlerini kullanan sitelerden ve uygulamalardan gelen bilgileri nasıl kullandığı</a> sayfasında açıklanır.</p>

<h2>3. Çocuklar</h2>
<p>Uygulama 13 yaş altındaki çocuklara yönelik değildir ve çocuklardan bilerek kişisel bilgi toplamayız. Reklamlar
genel izleyiciye uygun içerikle sınırlıdır.</p>

<h2>4. Hakların</h2>
<p>Kişisel verilerinden hiçbirini tutmadığımız için bizim tarafımızda erişilecek, düzeltilecek ya da silinecek bir
veri yoktur. Google'ın reklam için işlediği veriler için Google'ın politikalarındaki ayarları kullanabilir ya da
iOS ayarlarından reklam tanımlayıcını sıfırlayabilirsin. 6698 sayılı KVKK kapsamındaki başvuruların için aşağıdaki
adresten bize ulaşabilirsin.</p>

<h2>5. Değişiklikler</h2>
<p>Bu politika değişirse bu sayfayı ve yukarıdaki yürürlük tarihini güncelleriz.</p>

<h2>6. İletişim</h2>
<p>Gizlilikle ilgili sorular: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
""",
    },
    "support": {
        "en": f"""
<h1>Marble Mosaic — Support</h1>
<p>Found a bug, have an idea, or need help? Write to us at
<a href="mailto:{CONTACT_EMAIL}?subject=Marble%20Mosaic">{CONTACT_EMAIL}</a>. Please include your iPhone model, iOS
version and the level number, and a screenshot if you can. We usually reply within a few days.</p>
<h2>Frequently asked</h2>
<h3>How do I play?</h3>
<p>Tap a tray on the board. Its marbles roll through the funnel and drop into the cup of the same color. Clear
every tray to complete the picture. If too many marbles are waiting, the funnel overflows and you can try again.</p>
<h3>What are mystery and frozen trays?</h3>
<p>Grey mystery trays hide their color until the tray in front of them is cleared. Frozen trays can't be tapped
until the number on them reaches zero — every move melts the ice a little.</p>
<h3>How do Undo and +2 Funnel work?</h3>
<p>You get 3 free undos in every level; after that an undo costs coins. +2 Funnel adds two extra spaces to the
funnel once per level. If you don't have enough coins, you can watch an optional ad instead.</p>
<h3>How do I earn coins?</h3>
<p>Finish a level for the first time, and come back every day for the daily reward — it grows over 7 days in a row.</p>
<h3>Where is my progress saved?</h3>
<p>On your device. If you delete the app, your progress is deleted too.</p>
<h3>How do I turn off music, sounds or vibration, or change the language?</h3>
<p>Tap the gear button at the top right. Music, sound effects, vibration and language are all there.</p>
<h3>Do I have to watch ads?</h3>
<p>Rewarded ads are always optional. From level 4, a short ad may appear between levels from time to time.</p>
""",
        "tr": f"""
<h1>Marble Mosaic — Destek</h1>
<p>Bir hata mı buldun, bir fikrin mi var ya da yardım mı lazım? Bize
<a href="mailto:{CONTACT_EMAIL}?subject=Marble%20Mosaic">{CONTACT_EMAIL}</a> adresinden yaz. Lütfen iPhone modelini,
iOS sürümünü ve seviye numarasını, mümkünse bir ekran görüntüsü ekle. Genelde birkaç gün içinde dönüyoruz.</p>
<h2>Sık sorulanlar</h2>
<h3>Nasıl oynanır?</h3>
<p>Tahtadaki bir tepsiye dokun. Bilyeleri huniden geçip aynı renkteki bardağa düşer. Bütün tepsileri temizleyince
resim tamamlanır. Bekleyen bilye çok olursa huni taşar ve seviyeyi yeniden denersin.</p>
<h3>Gizli ve buzlu tepsiler nedir?</h3>
<p>Gri gizli tepsilerin rengi, önlerindeki tepsi alınana kadar görünmez. Buzlu tepsilere üstlerindeki sayı sıfıra
inene kadar dokunulamaz; her hamlede buz biraz erir.</p>
<h3>Geri Al ve +2 Huni nasıl çalışır?</h3>
<p>Her seviyede 3 geri alma hakkın var; sonrasında geri almak altınla olur. +2 Huni, seviye başına bir kez huniye
iki yer ekler. Altının yetmezse isteğe bağlı bir reklam izleyerek de alabilirsin.</p>
<h3>Altını nasıl kazanırım?</h3>
<p>Bir seviyeyi ilk kez bitirince altın kazanırsın. Her gün gelip günlük ödülünü de topla; 7 gün üst üste gelince
ödül büyür.</p>
<h3>İlerlemem nerede saklanıyor?</h3>
<p>Cihazında. Uygulamayı silersen ilerlemen de silinir.</p>
<h3>Müziği, sesleri ya da titreşimi nasıl kapatırım, dili nasıl değiştiririm?</h3>
<p>Sağ üstteki dişli butonuna dokun. Müzik, ses efektleri, titreşim ve dil orada.</p>
<h3>Reklam izlemek zorunda mıyım?</h3>
<p>Ödüllü reklamlar her zaman isteğe bağlıdır. 4. seviyeden sonra seviyeler arasında zaman zaman kısa bir reklam
çıkabilir.</p>
""",
    },
}

GAMES = [TINY_COURIERS, MARBLE_MOSAIC]


# ---------------------------------------------------------------- sayfa iskeleti

def page(lang: str, title: str, body: str, depth: int, other_href: str, desc: str, game: dict | None) -> str:
    t = T[lang]
    up = "../" * depth
    tr = "" if lang == "en" else "tr/"
    if game:  # oyun sayfaları: o oyunun tanıtım, gizlilik ve destek bağlantıları
        s = game["slug"]
        links = (f'  <a href="{up}{s}/{tr}">{game["name"]}</a>\n'
                 f'  <a href="{up}{s}/privacy/{tr}">{t["privacy"]}</a>\n'
                 f'  <a href="{up}{s}/support/{tr}">{t["support"]}</a>')
    else:  # ana sayfa: oyunlar
        links = "\n".join(f'  <a href="{up}{g["slug"]}/{tr}">{g["name"]}</a>' for g in GAMES)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{up}assets/style.css">
<link rel="icon" href="{up}assets/img/favicon.png">
<link rel="apple-touch-icon" href="{up}assets/img/apple-touch-icon.png">
</head>
<body>
<div class="wrap">
<header class="top">
  <a class="brand" href="{up}">Furog Games</a>
  <nav class="lang"><a href="{other_href}" hreflang="{t['other']}">{t['other_name']}</a></nav>
</header>
<main>
{body}
</main>
<footer>
  <span>{t['footer']}</span>
{links}
</footer>
</div>
</body>
</html>
"""


def game_body(game: dict, lang: str, depth: int) -> str:
    t = T[lang]
    g = game["text"][lang]
    up = "../" * depth
    name = game["name"]
    btn = (f'<a class="button" href="{game["app_store_url"]}">{t["store"]}</a>' if game["app_store_url"]
           else f'<span class="button soon">{t["soon"]}</span>')
    feats = "\n".join(f"  <li><b>{a}</b>{b}</li>" for a, b in g["features"])
    shots = "\n".join(f'  <img src="{up}assets/img/{f.format(lang=lang)}" alt="{name} screenshot" width="540" height="1170" loading="lazy">'
                      for f in game["shots"])
    return f"""<section class="hero">
  <img class="icon" src="{up}assets/img/{game['icon']}" alt="{name} app icon" width="148" height="148">
  <div>
    <h1>{name}</h1>
    <p class="lead">{g['tagline']} {g['lead']}</p>
    {btn}
  </div>
</section>
<div class="shots">
{shots}
</div>
<h2>{t['features_title']}</h2>
<ul class="features">
{feats}
</ul>"""


def home_body(lang: str, depth: int) -> str:
    up = "../" * depth
    tr = "" if lang == "en" else "tr/"
    cards = "\n".join(f"""<a class="card" href="{up}{g['slug']}/{tr}">
  <img src="{up}assets/img/{g['icon']}" alt="" width="96" height="96">
  <div><b>{g['name']}</b><span>{g['text'][lang]['tagline']}</span></div>
</a>""" for g in GAMES)
    return f"""<h1>Furog Games</h1>
<p class="lead">{T['en']['home_desc']} · {T['tr']['home_desc']}</p>
{cards}"""


def write(rel: str, html: str) -> None:
    p = ROOT / rel / "index.html" if rel else ROOT / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")


def main() -> None:
    # Ana sayfa (stüdyo): / ve /tr/
    write("", page("en", "Furog Games", home_body("en", 0), 0, "tr/", "Furog Games — small, cozy games.", None))
    write("tr", page("tr", "Furog Games", home_body("tr", 1), 1, "../", "Furog Games — küçük, sıcak oyunlar.", None))
    for game in GAMES:
        s, name = game["slug"], game["name"]
        for lang in ("en", "tr"):
            t = T[lang]
            sub = "" if lang == "en" else "/tr"
            d = 1 if lang == "en" else 2
            other = "tr/" if lang == "en" else "../"
            write(f"{s}{sub}", page(lang, name, game_body(game, lang, d), d, other, game["text"][lang]["tagline"], game))
            write(f"{s}/privacy{sub}", page(lang, f"{t['privacy']} — {name}",
                  f'<article class="doc">{game["privacy"][lang]}</article>', d + 1, other, t["privacy"], game))
            write(f"{s}/support{sub}", page(lang, f"{t['support']} — {name}",
                  f'<article class="doc">{game["support"][lang]}</article>', d + 1, other, t["support"], game))
    print("ok")


if __name__ == "__main__":
    main()
