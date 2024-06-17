import datetime


template = """
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>http://clipboard-js.vercel.app/transfer</loc>
      <lastmod>{date}</lastmod>
      <changefreq>monthly</changefreq>
      <priority>1.0</priority>
   </url>
</urlset>
"""

with open("public/sitemap.xml", "w") as f:
    new_text = template.format(date=datetime.datetime.now().isoformat())
    f.write(new_text)
    print(f"Updated the sitemap with:\n{new_text}")