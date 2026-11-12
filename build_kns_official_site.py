import os
import io
import base64
from PIL import Image

def get_opt_b64(path, max_dim=600, quality=85):
    if not os.path.exists(path):
        return ''
    try:
        img = Image.open(path)
        img.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        if img.mode in ('RGBA', 'P') and path.lower().endswith('.png'):
            img.save(buf, format='PNG', optimize=True)
            mime = 'image/png'
        else:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(buf, format='JPEG', quality=quality, optimize=True)
            mime = 'image/jpeg'
        data = buf.getvalue()
        return f'data:{mime};base64,{base64.b64encode(data).decode("utf-8")}'
    except Exception as e:
        print(f"Error encoding {path}: {e}")
        return ''

print("Encoding real original product photography extracted from KNS Master Catalogue...")
img_dir = 'E:/knsenterprise_repo/real_images'

# Real product photos from catalogue
img_jk = get_opt_b64(os.path.join(img_dir, 'p8_img2_500x500.png'), 500)
img_notebook = get_opt_b64(os.path.join(img_dir, 'p8_img3_400x300.png'), 500)
img_stapler = get_opt_b64(os.path.join(img_dir, 'p8_img4_400x620.png'), 500)
img_boxfile = get_opt_b64(os.path.join(img_dir, 'p8_img5_2000x2000.png'), 600)
img_taski = get_opt_b64(os.path.join(img_dir, 'p9_img2_722x1000.png'), 600)
img_trolley = get_opt_b64(os.path.join(img_dir, 'p9_img3_1000x1000.png'), 600)
img_dispenser = get_opt_b64(os.path.join(img_dir, 'p9_img4_600x400.png'), 500)
img_trashbags = get_opt_b64(os.path.join(img_dir, 'p9_img5_1024x1024.png'), 600)

# Real sector photography from catalogue
img_school = get_opt_b64(os.path.join(img_dir, 'p4_img2_800x450.png'), 600)
img_office = get_opt_b64(os.path.join(img_dir, 'p5_img2_800x534.png'), 600)
img_hospital = get_opt_b64(os.path.join(img_dir, 'p6_img2_800x544.png'), 600)
img_manpower = get_opt_b64(os.path.join(img_dir, 'p7_img2_800x533.png'), 600)

# Brand and verified clients
logo_b64 = get_opt_b64('E:/knsenterprise_repo/kns_logo.png', 420)
clients = {
    'rainbow': get_opt_b64('E:/knsenterprise_repo/rainbow.png', 280),
    'nri': get_opt_b64('E:/knsenterprise_repo/nri-academy.png', 280),
    'esic': get_opt_b64('E:/knsenterprise_repo/esic.png', 280),
    'spa': get_opt_b64('E:/knsenterprise_repo/spa.png', 280),
    'ravindra': get_opt_b64('E:/knsenterprise_repo/ravindra-bharthi.png', 280),
    'model_dairy': get_opt_b64('E:/knsenterprise_repo/model-dairy.png', 280),
    'birlanu': get_opt_b64('E:/knsenterprise_repo/birlanu.png', 280),
    'phcc': get_opt_b64('E:/knsenterprise_repo/phcc.png', 280)
}

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>KNS Enterprise | Institutional Wholesale Supply Partner • Vijayawada</title>
    <meta name="description" content="Wholesale Copier Paper, Examination Stationery, and Commercial Housekeeping Consumables for Schools, Colleges, Hospitals & Corporate Offices in Vijayawada & AP.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-body: #FFFFFF;
            --bg-subtle: #F8FAFC;
            --navy-primary: #0F172A;
            --navy-dark: #0A0F1D;
            --text-main: #0F172A;
            --text-secondary: #475569;
            --text-muted: #64748B;
            --gold-primary: #9A7B1C;
            --gold-subtle: #FDF9EE;
            --gold-border: #E8D390;
            --border-light: #E2E8F0;
            --whatsapp-green: #15803D;
            --whatsapp-bg: #DCFCE7;
            --radius-card: 16px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }}

        body {{
            background-color: var(--bg-body);
            color: var(--text-main);
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.6;
            overflow-x: hidden;
            padding-bottom: 84px;
        }}

        /* Clean Top Governance Bar */
        .top-compliance-bar {{
            background: var(--navy-dark);
            color: #E2E8F0;
            padding: 9px 20px;
            font-size: 12px;
            font-weight: 600;
            text-align: center;
            letter-spacing: 0.02em;
        }}
        .top-compliance-bar span.gold {{
            color: #FACC15;
            font-weight: 700;
        }}
        .top-compliance-bar .divider {{
            margin: 0 8px;
            opacity: 0.35;
        }}

        /* Header Navigation */
        header.site-header {{
            position: sticky;
            top: 0;
            z-index: 999;
            background: #FFFFFF;
            border-bottom: 1px solid var(--border-light);
            padding: 14px 24px;
        }}
        .nav-container {{
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .brand-cluster {{
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: var(--navy-primary);
        }}
        .brand-logo-img {{
            width: 44px;
            height: 44px;
            object-fit: contain;
            border-radius: 8px;
            background: #fff;
            padding: 2px;
            border: 1px solid var(--border-light);
        }}
        .brand-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 20px;
            font-weight: 800;
            letter-spacing: -0.01em;
            color: var(--navy-primary);
            line-height: 1.1;
        }}
        .brand-tagline {{
            font-size: 11px;
            font-weight: 700;
            color: var(--gold-primary);
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }}
        .nav-actions {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .btn-call-nav {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #F1F5F9;
            color: var(--navy-primary);
            text-decoration: none;
            padding: 9px 15px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: 700;
            border: 1px solid var(--border-light);
        }}
        .btn-whatsapp-nav {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--whatsapp-green);
            color: #FFFFFF;
            text-decoration: none;
            padding: 9px 18px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: 800;
        }}

        .content-wrap {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}

        /* Hero Section */
        .hero-section {{
            padding: 48px 0 36px;
            background: var(--bg-body);
        }}
        .hero-grid {{
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 40px;
            align-items: center;
        }}
        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: var(--gold-subtle);
            border: 1px solid var(--gold-border);
            padding: 6px 14px;
            border-radius: 50px;
            font-size: 12px;
            font-weight: 700;
            color: var(--gold-primary);
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin-bottom: 16px;
        }}
        .hero-heading {{
            font-family: 'Outfit', sans-serif;
            font-size: clamp(32px, 4.2vw, 48px);
            font-weight: 800;
            line-height: 1.15;
            color: var(--navy-primary);
            margin-bottom: 16px;
            letter-spacing: -0.02em;
        }}
        .hero-heading span.highlight {{
            color: var(--gold-primary);
        }}
        .hero-sub {{
            font-size: 16px;
            color: var(--text-secondary);
            margin-bottom: 26px;
            line-height: 1.6;
        }}
        .hero-cta-cluster {{
            display: flex;
            align-items: center;
            gap: 14px;
            flex-wrap: wrap;
        }}
        .btn-primary-wa {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: var(--whatsapp-green);
            color: #FFFFFF;
            text-decoration: none;
            padding: 14px 24px;
            border-radius: 12px;
            font-size: 15px;
            font-weight: 800;
        }}
        .btn-secondary-pdf {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: #FFFFFF;
            color: var(--navy-primary);
            text-decoration: none;
            padding: 14px 22px;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 700;
            border: 1px solid var(--border-light);
        }}

        /* Hero Primary Product Spotlight (One Product Steps Forward) */
        .spotlight-card {{
            background: var(--bg-subtle);
            border: 1.5px solid var(--gold-border);
            border-radius: 20px;
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}
        .spotlight-badge {{
            align-self: flex-start;
            background: #B45309;
            color: #FFFFFF;
            font-size: 11px;
            font-weight: 800;
            text-transform: uppercase;
            padding: 4px 10px;
            border-radius: 6px;
            letter-spacing: 0.06em;
        }}
        .spotlight-img-wrap {{
            width: 100%;
            height: 220px;
            background: #FFFFFF;
            border-radius: 14px;
            border: 1px solid var(--border-light);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 16px;
            overflow: hidden;
        }}
        .spotlight-img-wrap img {{
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }}
        .spotlight-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 20px;
            font-weight: 800;
            color: var(--navy-primary);
        }}
        .spotlight-desc {{
            font-size: 13px;
            color: var(--text-secondary);
            line-height: 1.5;
        }}

        /* Section Headings */
        .section-header {{
            text-align: center;
            margin: 48px 0 28px;
        }}
        .section-tag {{
            font-size: 11px;
            font-weight: 800;
            color: var(--gold-primary);
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 6px;
        }}
        .section-title {{
            font-family: 'Outfit', sans-serif;
            font-size: clamp(24px, 3.6vw, 34px);
            font-weight: 800;
            color: var(--navy-primary);
            letter-spacing: -0.01em;
        }}

        /* Real Products Grid (Clean White Cards With Real Product Photography) */
        .real-product-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 20px;
            margin-bottom: 48px;
        }}
        .product-item-card {{
            background: #FFFFFF;
            border: 1px solid var(--border-light);
            border-radius: 16px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .product-img-box {{
            width: 100%;
            height: 180px;
            background: #F8FAFC;
            border-radius: 12px;
            border: 1px solid #EDF2F7;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 12px;
            margin-bottom: 14px;
            overflow: hidden;
        }}
        .product-img-box img {{
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }}
        .item-tag {{
            font-size: 10px;
            font-weight: 800;
            color: var(--gold-primary);
            text-transform: uppercase;
            margin-bottom: 4px;
            display: block;
        }}
        .item-name {{
            font-family: 'Outfit', sans-serif;
            font-size: 16px;
            font-weight: 800;
            color: var(--navy-primary);
            line-height: 1.3;
            margin-bottom: 6px;
        }}
        .item-spec {{
            font-size: 12px;
            color: var(--text-secondary);
            line-height: 1.45;
            margin-bottom: 14px;
            flex-grow: 1;
        }}
        .btn-inquire-item {{
            background: #F1F5F9;
            color: var(--navy-primary);
            text-decoration: none;
            padding: 9px 12px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 800;
            text-align: center;
            border: 1px solid var(--border-light);
            display: block;
        }}
        .btn-inquire-item:hover {{
            background: var(--whatsapp-green);
            color: #FFFFFF;
            border-color: var(--whatsapp-green);
        }}

        /* Real Campus Sectors Showcase (From Catalogue Page 4,5,6,7) */
        .sectors-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 20px;
            margin-bottom: 48px;
        }}
        .sector-card {{
            background: #FFFFFF;
            border: 1px solid var(--border-light);
            border-radius: 16px;
            overflow: hidden;
        }}
        .sector-img-box {{
            width: 100%;
            height: 180px;
            overflow: hidden;
        }}
        .sector-img-box img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .sector-body {{
            padding: 18px;
        }}
        .sector-name {{
            font-family: 'Outfit', sans-serif;
            font-size: 16px;
            font-weight: 800;
            color: var(--navy-primary);
            margin-bottom: 4px;
        }}
        .sector-desc {{
            font-size: 12px;
            color: var(--text-secondary);
            line-height: 1.45;
        }}

        /* Institutional Clients Wall */
        .clients-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 16px;
            margin-bottom: 48px;
        }}
        .client-box {{
            background: #FFFFFF;
            border: 1px solid var(--border-light);
            border-radius: 14px;
            padding: 16px;
            display: flex;
            align-items: flex-start;
            gap: 14px;
        }}
        .client-logo-wrap {{
            width: 54px;
            height: 54px;
            border-radius: 10px;
            background: #FFFFFF;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 6px;
            flex-shrink: 0;
            border: 1px solid var(--border-light);
        }}
        .client-logo-wrap img {{
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }}
        .client-info {{
            flex: 1;
        }}
        .client-cat-tag {{
            font-size: 10px;
            font-weight: 800;
            color: var(--gold-primary);
            text-transform: uppercase;
            margin-bottom: 2px;
        }}
        .client-name {{
            font-weight: 800;
            font-size: 13px;
            color: var(--navy-primary);
            line-height: 1.25;
            margin-bottom: 4px;
        }}
        .client-supply-scope {{
            font-size: 11px;
            color: var(--text-secondary);
            line-height: 1.4;
        }}

        /* Corporate Footer */
        footer.site-footer {{
            background: var(--navy-dark);
            color: #94A3B8;
            padding: 40px 20px 24px;
            font-size: 13px;
        }}
        .footer-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 28px;
            margin-bottom: 28px;
        }}
        .footer-col-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 15px;
            font-weight: 700;
            color: #FFFFFF;
            margin-bottom: 12px;
        }}
        .footer-links {{
            list-style: none;
        }}
        .footer-links li {{
            margin-bottom: 8px;
        }}
        .footer-links a {{
            color: #CBD5E1;
            text-decoration: none;
        }}
        .footer-bottom-bar {{
            text-align: center;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            padding-top: 20px;
            font-size: 12px;
            color: #64748B;
        }}

        /* Mobile Floating Bottom Bar */
        .mobile-bottom-bar {{
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background: #FFFFFF;
            border-top: 1px solid var(--border-light);
            padding: 10px 16px;
            display: flex;
            align-items: center;
            justify-content: space-around;
            gap: 10px;
        }}
        .bottom-action-btn {{
            flex: 1;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 12px;
            border-radius: 12px;
            font-size: 13px;
            font-weight: 800;
            text-decoration: none;
        }}
        .btn-wa-bottom {{
            background: var(--whatsapp-green);
            color: #FFFFFF;
        }}
        .btn-call-bottom {{
            background: #F1F5F9;
            color: var(--navy-primary);
            border: 1px solid var(--border-light);
        }}
        .btn-catalog-bottom {{
            background: var(--gold-subtle);
            color: var(--gold-primary);
            border: 1px solid var(--gold-border);
        }}

        @media (max-width: 900px) {{
            .hero-grid {{
                grid-template-columns: 1fr;
                gap: 24px;
            }}
        }}

        @media (min-width: 769px) {{
            .mobile-bottom-bar {{
                display: none;
            }}
            body {{
                padding-bottom: 0;
            }}
        }}
    </style>
</head>
<body>

    <!-- Top Governance Bar -->
    <div class="top-compliance-bar">
        CENTRAL INSTITUTIONAL PROCUREMENT HUB <span class="divider">•</span> ANDHRA PRADESH
        <span class="divider">•</span> GOVT GSTIN: <span class="gold">37AAHCK6147F1ZS</span>
        <span class="divider">•</span> FOUNDED: 2025 <span class="divider">•</span> VIJAYAWADA
    </div>

    <!-- Header Navigation -->
    <header class="site-header">
        <div class="nav-container">
            <a href="#" class="brand-cluster">
                <img src="{logo_b64}" alt="KNS Enterprise Logo" class="brand-logo-img">
                <div class="brand-text-block">
                    <span class="brand-title">KNS ENTERPRISE</span>
                    <span class="brand-tagline">Stationery • Housekeeping • Services</span>
                </div>
            </a>
            <div class="nav-actions">
                <a href="tel:+919494066186" class="btn-call-nav">
                    📞 94940 66186
                </a>
                <a href="https://wa.me/919160877373?text=Hi%20Sunil%2C%20we%20need%20a%20wholesale%20quotation%20for%20our%20institution." class="btn-whatsapp-nav">
                    💬 WhatsApp Desk
                </a>
            </div>
        </div>
    </header>

    <!-- Clean Light Hero Section -->
    <section class="hero-section">
        <div class="content-wrap">
            <div class="hero-grid">
                <div>
                    <div class="hero-badge">
                        Central Institutional Desk • Vijayawada
                    </div>
                    <h1 class="hero-heading">
                        Institutional Wholesale Supplies for <br>
                        <span class="highlight">Schools, Hospitals & Corporates</span>
                    </h1>
                    <p class="hero-sub">
                        Direct mill-allocated Copier Paper, Examination Stationery, and Commercial Housekeeping Consumables. Backed by guaranteed same-day corridor delivery and verified GST input tax credit across Vijayawada, Guntur & Corridors.
                    </p>
                    <div class="hero-cta-cluster">
                        <a href="https://wa.me/919160877373?text=Hi%20Sunil%2C%20please%20share%20institutional%20quotation%20for%20our%20campus." class="btn-primary-wa">
                            💬 Send Requirement on WhatsApp
                        </a>
                        <a href="KNS_MASTER_WHOLESALE_CATALOGUE_2026.pdf" download class="btn-secondary-pdf">
                            📄 Download Master Catalogue (PDF)
                        </a>
                    </div>
                </div>

                <!-- Spotlight Card: One Product Steps Forward (Rule 3) -->
                <div class="spotlight-card">
                    <span class="spotlight-badge">Mill-Direct Priority Allocation</span>
                    <div class="spotlight-img-wrap">
                        <img src="{img_jk}" alt="JK Copier Paper 75 GSM">
                    </div>
                    <div class="spotlight-title">JK Copier Paper 75 GSM (A4)</div>
                    <div class="spotlight-desc">
                        10 Reams/Box (5,000 Sheets). High-speed offset & laser printing grade with ultra-pure white brightness. Direct mill allocation for campus examinations and hospital diagnostic records.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Real Products Section (Clean White Cards With Real Product Art - Rule 4) -->
    <section class="content-wrap">
        <div class="section-header">
            <div class="section-tag">Direct Mill & Factory Allocation</div>
            <h2 class="section-title">Essential Campus Consumables</h2>
        </div>

        <div class="real-product-grid">

            <!-- Item 1: JK Paper -->
            <div class="product-item-card">
                <div>
                    <div class="product-img-box">
                        <img src="{img_jk}" alt="JK Copier Paper">
                    </div>
                    <span class="item-tag">Copier Paper</span>
                    <div class="item-name">JK Copier 75 GSM (A4)</div>
                    <div class="item-spec">500 Sheets/Ream • 10 Reams/Box • High-speed jam-free laser printing.</div>
                </div>
                <a href="https://wa.me/919160877373?text=Quote%20JK%20Copier%20Paper" class="btn-inquire-item">Inquire Wholesale Rate</a>
            </div>

            <!-- Item 2: Spiral Notebook -->
            <div class="product-item-card">
                <div>
                    <div class="product-img-box">
                        <img src="{img_notebook}" alt="KNS Deluxe Spiral Notebook">
                    </div>
                    <span class="item-tag">Academic Stationery</span>
                    <div class="item-name">KNS Deluxe Spiral Notebook (A4)</div>
                    <div class="item-spec">300 Pages • 70 GSM Sunshine Paper • Twin-wire rust-proof spiral.</div>
                </div>
                <a href="https://wa.me/919160877373?text=Quote%20Spiral%20Notebooks" class="btn-inquire-item">Inquire Wholesale Rate</a>
            </div>

            <!-- Item 3: Diversey Taski R2 -->
            <div class="product-item-card">
                <div>
                    <div class="product-img-box">
                        <img src="{img_taski}" alt="Diversey Taski R2">
                    </div>
                    <span class="item-tag">Commercial Chemicals</span>
                    <div class="item-name">Diversey Taski R2 Cleaner (5L)</div>
                    <div class="item-spec">Concentrated hard surface formulation for granite, marble & tiles.</div>
                </div>
                <a href="https://wa.me/919160877373?text=Quote%20Taski%20R2%205L" class="btn-inquire-item">Inquire Wholesale Rate</a>
            </div>

            <!-- Item 4: Double Bucket Wringer Trolley -->
            <div class="product-item-card">
                <div>
                    <div class="product-img-box">
                        <img src="{img_trolley}" alt="Double Bucket Wringer Trolley">
                    </div>
                    <span class="item-tag">Janitorial Equipment</span>
                    <div class="item-name">Double-Bucket Wringer Trolley</div>
                    <div class="item-spec">40L Capacity (20L Clean + 20L Dirty) • Mechanical down-press wringer.</div>
                </div>
                <a href="https://wa.me/919160877373?text=Quote%20Wringer%20Trolley" class="btn-inquire-item">Inquire Wholesale Rate</a>
            </div>

            <!-- Item 5: Lever Arch File -->
            <div class="product-item-card">
                <div>
                    <div class="product-img-box">
                        <img src="{img_boxfile}" alt="Heavy Duty Lever Arch File">
                    </div>
                    <span class="item-tag">Archival Systems</span>
                    <div class="item-name">Heavy-Duty Lever Arch File (A4)</div>
                    <div class="item-spec">75mm Spine • 500 Sheets Capacity • Rigid PVC laminated board.</div>
                </div>
                <a href="https://wa.me/919160877373?text=Quote%20Lever%20Arch%20Files" class="btn-inquire-item">Inquire Wholesale Rate</a>
            </div>

            <!-- Item 6: Desk Procurement Kit -->
            <div class="product-item-card">
                <div>
                    <div class="product-img-box">
                        <img src="{img_stapler}" alt="Kangaro Stapler & Desk Kit">
                    </div>
                    <span class="item-tag">Desk Hardware</span>
                    <div class="item-name">Executive Desk Procurement Set</div>
                    <div class="item-spec">Kangaro HD staplers, commercial calculators & industrial tapes.</div>
                </div>
                <a href="https://wa.me/919160877373?text=Quote%20Executive%20Desk%20Kit" class="btn-inquire-item">Inquire Wholesale Rate</a>
            </div>

            <!-- Item 7: Touchless Dispenser -->
            <div class="product-item-card">
                <div>
                    <div class="product-img-box">
                        <img src="{img_dispenser}" alt="Touchless Dispenser">
                    </div>
                    <span class="item-tag">Hygiene Systems</span>
                    <div class="item-name">Automatic Touchless Dispenser</div>
                    <div class="item-spec">1000ml Liquid / Gel capacity • Infrared motion sensor for clinics.</div>
                </div>
                <a href="https://wa.me/919160877373?text=Quote%20Touchless%20Dispenser" class="btn-inquire-item">Inquire Wholesale Rate</a>
            </div>

            <!-- Item 8: Bio-Medical Bags -->
            <div class="product-item-card">
                <div>
                    <div class="product-img-box">
                        <img src="{img_trashbags}" alt="Bio-Medical Trash Bags">
                    </div>
                    <span class="item-tag">Waste Management</span>
                    <div class="item-name">Bio-Medical Trash Bags (Pack of 50)</div>
                    <div class="item-spec">30x50 Inches • 50 Microns Heavy-Duty • CPCB Compliant color codes.</div>
                </div>
                <a href="https://wa.me/919160877373?text=Quote%20Bio-Medical%20Trash%20Bags" class="btn-inquire-item">Inquire Wholesale Rate</a>
            </div>

        </div>
    </section>

    <!-- Real Operational Scope (Pages 4,5,6,7 from Catalogue) -->
    <section class="content-wrap">
        <div class="section-header">
            <div class="section-tag">Campus Procurement Corridors</div>
            <h2 class="section-title">Specialized Institutional Supply Scope</h2>
        </div>

        <div class="sectors-grid">
            <div class="sector-card">
                <div class="sector-img-box">
                    <img src="{img_school}" alt="Schools and Colleges">
                </div>
                <div class="sector-body">
                    <div class="sector-name">Schools & Colleges</div>
                    <div class="sector-desc">Classroom stationery, student registers, examination paper dispatch, and campus dining hall sanitation.</div>
                </div>
            </div>

            <div class="sector-card">
                <div class="sector-img-box">
                    <img src="{img_office}" alt="Commercial & IT Offices">
                </div>
                <div class="sector-body">
                    <div class="sector-name">Commercial & IT Offices</div>
                    <div class="sector-desc">Executive boardroom kits, reception supplies, workstation desk organizers, and daily housekeeping chemicals.</div>
                </div>
            </div>

            <div class="sector-card">
                <div class="sector-img-box">
                    <img src="{img_hospital}" alt="Healthcare & Hospitals">
                </div>
                <div class="sector-body">
                    <div class="sector-name">Healthcare & Hospitals</div>
                    <div class="sector-desc">Sterile patient ward sanitization, touchless dispensers, CPCB bio-medical waste bags, and diagnostic paper.</div>
                </div>
            </div>

            <div class="sector-card">
                <div class="sector-img-box">
                    <img src="{img_manpower}" alt="Facility & Manpower Support">
                </div>
                <div class="sector-body">
                    <div class="sector-name">Facility & Commercial Care</div>
                    <div class="sector-desc">Uniformed commercial care, mechanized floor scrubbing consumables, and high-RPM surface maintenance.</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Institutional Clients Wall -->
    <section class="content-wrap">
        <div class="section-header">
            <div class="section-tag">Institutional Proof & Credibility</div>
            <h2 class="section-title">Supplying 50+ Premier Campuses Across AP</h2>
        </div>

        <div class="clients-grid">
            <!-- Rainbow -->
            <div class="client-box">
                <div class="client-logo-wrap">
                    <img src="{clients['rainbow']}" alt="Rainbow Children's Medicare">
                </div>
                <div class="client-info">
                    <div class="client-cat-tag">Super-Speciality Healthcare</div>
                    <div class="client-name">Rainbow Children’s Medicare Ltd</div>
                    <div class="client-supply-scope">Pediatric ward cleaning chemicals, automatic touchless hand sanitization systems, embossed M-fold paper towels.</div>
                </div>
            </div>

            <!-- NRI Academy -->
            <div class="client-box">
                <div class="client-logo-wrap">
                    <img src="{clients['nri']}" alt="NRI Academy of Sciences">
                </div>
                <div class="client-info">
                    <div class="client-cat-tag">Medical College & Hospital</div>
                    <div class="client-name">NRI Academy of Sciences</div>
                    <div class="client-supply-scope">Hospital surface disinfectants, Diversey Taski suite, CPCB color-coded bio-hazard waste bags & medical forms.</div>
                </div>
            </div>

            <!-- SPA Vijayawada -->
            <div class="client-box">
                <div class="client-logo-wrap">
                    <img src="{clients['spa']}" alt="School of Planning and Architecture (SPA)">
                </div>
                <div class="client-info">
                    <div class="client-cat-tag">Institute of National Importance</div>
                    <div class="client-name">School of Planning & Architecture (SPA)</div>
                    <div class="client-supply-scope">Architectural drawing & copier papers, administrative registers, archival box files & scrubbing consumables.</div>
                </div>
            </div>

            <!-- Ravindra Bharathi -->
            <div class="client-box">
                <div class="client-logo-wrap">
                    <img src="{clients['ravindra']}" alt="Ravindra Bharathi Public School">
                </div>
                <div class="client-info">
                    <div class="client-cat-tag">Premier Educational Network</div>
                    <div class="client-name">Ravindra Bharathi Public School</div>
                    <div class="client-supply-scope">Institutional stationery, student registers, JK Copier 75 GSM reams, campus restroom hygiene chemicals.</div>
                </div>
            </div>

            <!-- ESIC Hospital -->
            <div class="client-box">
                <div class="client-logo-wrap">
                    <img src="{clients['esic']}" alt="ESIC Hospital">
                </div>
                <div class="client-info">
                    <div class="client-cat-tag">Government & Public Sector</div>
                    <div class="client-name">ESIC Hospital (Govt. of India)</div>
                    <div class="client-supply-scope">Heavy-duty hospital disinfection chemicals, janitorial wringer trolleys, continuous printing stationery & office files.</div>
                </div>
            </div>

            <!-- Model Dairy -->
            <div class="client-box">
                <div class="client-logo-wrap">
                    <img src="{clients['model_dairy']}" alt="Model Dairy Pvt Ltd">
                </div>
                <div class="client-info">
                    <div class="client-cat-tag">Corporate & Processing</div>
                    <div class="client-name">Model Dairy Pvt Ltd</div>
                    <div class="client-supply-scope">Food-grade sanitizers, plant hygiene consumables, microfiber floor maintenance systems & warehouse ledgers.</div>
                </div>
            </div>

            <!-- BirlaNu -->
            <div class="client-box">
                <div class="client-logo-wrap">
                    <img src="{clients['birlanu']}" alt="BirlaNu Ltd">
                </div>
                <div class="client-info">
                    <div class="client-cat-tag">CK Birla Group Enterprise</div>
                    <div class="client-name">BirlaNu Ltd</div>
                    <div class="client-supply-scope">Industrial degreasers, heavy floor cleaners, BOPP packaging tapes, stretch film & commercial registers.</div>
                </div>
            </div>

            <!-- PHCC -->
            <div class="client-box">
                <div class="client-logo-wrap">
                    <img src="{clients['phcc']}" alt="Peddeswar Health Care Center">
                </div>
                <div class="client-info">
                    <div class="client-cat-tag">Clinical Diagnostics</div>
                    <div class="client-name">Peddeswar Health Care Center (PHCC)</div>
                    <div class="client-supply-scope">Antimicrobial floor wash, Grade-1 phenyle, bio-hazard garbage bags, pedal dustbins & administrative stationery.</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Corporate Footer -->
    <footer class="site-footer">
        <div class="content-wrap">
            <div class="footer-grid">
                <div>
                    <div class="footer-col-title">KNS ENTERPRISE</div>
                    <p style="font-size: 13px; line-height: 1.6; margin-bottom: 12px; color: #94A3B8;">
                        Premier Institutional B2B Wholesale Supply Partner for Office Stationery, Copier Paper, and Commercial Housekeeping Consumables.
                    </p>
                    <p style="font-size: 12px; color: #FACC15;">
                        Govt. GSTIN: 37AAHCK6147F1ZS <br>
                        Founded: 2025 • Vijayawada, Andhra Pradesh
                    </p>
                </div>
                <div>
                    <div class="footer-col-title">Active Service Corridors</div>
                    <ul class="footer-links">
                        <li>• Vijayawada Central & Auto Nagar</li>
                        <li>• Guntur & Mangalagiri Corridor</li>
                        <li>• Tenali & Vuyyuru Belt</li>
                        <li>• Eluru & Gannavaram Airport Zone</li>
                        <li>• Amaravathi Capital Region</li>
                    </ul>
                </div>
                <div>
                    <div class="footer-col-title">Order & Procurement Desk</div>
                    <ul class="footer-links">
                        <li>📞 <strong>Hotline:</strong> <a href="tel:+919494066186">+91 94940 66186</a></li>
                        <li>💬 <strong>WhatsApp:</strong> <a href="https://wa.me/919160877373">+91 91608 77373</a></li>
                        <li>✉️ <strong>Email:</strong> <a href="mailto:knsenterprise2@gmail.com">knsenterprise2@gmail.com</a></li>
                        <li>📄 <strong>Catalogue:</strong> <a href="KNS_MASTER_WHOLESALE_CATALOGUE_2026.pdf" download>Download 2026 Master PDF</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom-bar">
                © 2026 KNS ENTERPRISE. All Rights Reserved. Institutional B2B Wholesale Supplier • Vijayawada, AP.
            </div>
        </div>
    </footer>

    <!-- Mobile Floating Bottom Action Bar -->
    <div class="mobile-bottom-bar">
        <a href="https://wa.me/919160877373?text=Hi%20Sunil%2C%20we%20need%20a%20wholesale%20quotation%20for%20our%20institution." class="bottom-action-btn btn-wa-bottom">
            💬 WhatsApp Quote
        </a>
        <a href="tel:+919494066186" class="bottom-action-btn btn-call-bottom">
            📞 Call Desk
        </a>
        <a href="KNS_MASTER_WHOLESALE_CATALOGUE_2026.pdf" download class="bottom-action-btn btn-catalog-bottom">
            📄 Catalogue
        </a>
    </div>

</body>
</html>
'''

output_path = 'E:/knsenterprise_repo/index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated clean, authentic corporate site with real product art at {output_path} ({len(html_content)} bytes)")
