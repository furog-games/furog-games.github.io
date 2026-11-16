"""Furog Games sitesini üretir (statik HTML). Çalıştır: python3 tools/build.py
Sayfalar: / · /tiny-couriers/ (+tr) · /tiny-couriers/privacy/ (+tr) · /tiny-couriers/support/ (+tr)
İletişim e-postası ve App Store bağlantısı aşağıdaki sabitlerde.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTACT_EMAIL = "marinariogroup@gmail.com"      # yayımlanacak destek e-postası
APP_STORE_URL = ""                  # yayına çıkınca: https://apps.apple.com/app/idXXXXXXXXX
EFFECTIVE = {"en": "November 16, 2026", "tr": "16 Kasım 2026"}

T = {
    "en": {
        "lang": "en", "other": "tr", "other_name": "Türkçe",
        "tagline": "Run a tiny delivery company on a floating sky-island city.",
        "lead": "Take orders from burger joints, bakeries and flower shops, send your couriers zipping "
                "across town on their scooters, collect the coins and grow your fleet — district by district.",
        "store": "Download on the App Store", "soon": "Coming soon to the App Store",
        "features_title": "What you do",
        "features": [
            ("Dispatch orders", "Pick the right courier for every order before it runs out of time."),
            ("Grow your fleet", "Hire couriers, sign contracts with local shops and unlock new districts."),
            ("Upgrade everything", "Faster scooters, more orders, auto-collect and a manager who works while you're away."),
            ("Pause and plan", "Freeze the map, assign everyone, then hit play and watch them go."),
        ],
        "privacy": "Privacy Policy", "support": "Support",
        "home_desc": "We make small, cozy games.",
        "footer": "© 2026 Furog Games",
    },
    "tr": {
        "lang": "tr", "other": "en", "other_name": "English",
        "tagline": "Gökyüzünde yüzen bir ada şehrinde minik bir kurye şirketi yönet.",
        "lead": "Burgerciden, fırından, çiçekçiden gelen siparişleri al; kuryelerini scooter'larıyla şehrin "
                "dört bir yanına gönder, paraları topla ve filonu mahalle mahalle büyüt.",
        "store": "App Store'dan indir", "soon": "Yakında App Store'da",
        "features_title": "Oyunda neler var",
        "features": [
            ("Siparişleri dağıt", "Her siparişi süresi dolmadan doğru kuryeye ata."),
            ("Filonu büyüt", "Kurye al, dükkânlarla sözleşme imzala, yeni mahalleler aç."),
            ("Her şeyi geliştir", "Hızlı scooterlar, daha çok sipariş, otomatik toplama ve sen yokken çalışan bir müdür."),
            ("Durdur ve planla", "Haritayı dondur, herkesi ata, sonra oynat ve kuryelerini izle."),
        ],
        "privacy": "Gizlilik Politikası", "support": "Destek",
        "home_desc": "Küçük, sıcak oyunlar yapıyoruz.",
        "footer": "© 2026 Furog Games",
    },
}

PRIVACY = {
    "en": f"""
<h1>Privacy Policy — Tiny Couriers</h1>
<p class="meta">Effective date: {EFFECTIVE['en']} · Developer: Furog Games</p>
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
<p class="meta">Yürürlük tarihi: {EFFECTIVE['tr']} · Geliştirici: Furog Games</p>
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
}

SUPPORT = {
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
}


def page(lang: str, title: str, body: str, depth: int, other_href: str, desc: str) -> str:
    t = T[lang]
    up = "../" * depth
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
  <a href="{up}tiny-couriers/{'' if lang == 'en' else 'tr/'}">Tiny Couriers</a>
  <a href="{up}tiny-couriers/privacy/{'' if lang == 'en' else 'tr/'}">{t['privacy']}</a>
  <a href="{up}tiny-couriers/support/{'' if lang == 'en' else 'tr/'}">{t['support']}</a>
</footer>
</div>
</body>
</html>
"""


def game_body(lang: str, depth: int) -> str:
    t = T[lang]
    up = "../" * depth
    btn = (f'<a class="button" href="{APP_STORE_URL}">{t["store"]}</a>' if APP_STORE_URL
           else f'<span class="button soon">{t["soon"]}</span>')
    feats = "\n".join(f"  <li><b>{a}</b>{b}</li>" for a, b in t["features"])
    shots = "\n".join(f'  <img src="{up}assets/img/shot-{k}.jpg" alt="Tiny Couriers screenshot" width="540" height="1170" loading="lazy">'
                      for k in ["play", "orders", "upgrades", "island"])
    return f"""<section class="hero">
  <img class="icon" src="{up}assets/img/tiny-couriers-icon.png" alt="Tiny Couriers app icon" width="148" height="148">
  <div>
    <h1>Tiny Couriers</h1>
    <p class="lead">{t['tagline']} {t['lead']}</p>
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


def write(rel: str, html: str) -> None:
    p = ROOT / rel / "index.html" if rel else ROOT / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")


def main() -> None:
    # Ana sayfa (stüdyo)
    home = f"""<h1>Furog Games</h1>
<p class="lead">{T['en']['home_desc']} · {T['tr']['home_desc']}</p>
<a class="card" href="tiny-couriers/">
  <img src="assets/img/tiny-couriers-icon.png" alt="" width="96" height="96">
  <div><b>Tiny Couriers</b><span>{T['en']['tagline']}</span></div>
</a>"""
    write("", page("en", "Furog Games", home, 0, "tiny-couriers/tr/", "Furog Games — small, cozy games."))
    for lang in ("en", "tr"):
        sub = "" if lang == "en" else "/tr"
        d = 1 if lang == "en" else 2
        other = lambda base: ("tr/" if lang == "en" else "../")
        write(f"tiny-couriers{sub}", page(lang, "Tiny Couriers", game_body(lang, d), d, other(""), T[lang]["tagline"]))
        write(f"tiny-couriers/privacy{sub}", page(lang, f"{T[lang]['privacy']} — Tiny Couriers",
              f'<article class="doc">{PRIVACY[lang]}</article>', d + 1, other(""), T[lang]["privacy"]))
        write(f"tiny-couriers/support{sub}", page(lang, f"{T[lang]['support']} — Tiny Couriers",
              f'<article class="doc">{SUPPORT[lang]}</article>', d + 1, other(""), T[lang]["support"]))
    print("ok")


if __name__ == "__main__":
    main()
