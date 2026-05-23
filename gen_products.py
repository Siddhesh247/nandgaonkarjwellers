import os
import json

PHONE = '919518356108'

OUT = r"C:\Users\ssnan\OneDrive\Desktop\Python Website\products"

os.makedirs(OUT, exist_ok=True)
# ── GOLD IMAGE SETS (4 images per product using Pexels jewellery photos)
GOLD_IMG_SETS = [
    [r"C:\Users\ssnan\OneDrive\Desktop\Python Website\product images gold\ChatGPT_Image_Dec_25__2025__09_51_17_PM-removebg-preview.png",
     "https://images.pexels.com/photos/10478906/pexels-photo-10478906.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/1191531/pexels-photo-1191531.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/691046/pexels-photo-691046.jpeg?auto=compress&w=800"],
    ["https://images.pexels.com/photos/691046/pexels-photo-691046.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/1191531/pexels-photo-1191531.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/10478867/pexels-photo-10478867.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/10478906/pexels-photo-10478906.jpeg?auto=compress&w=800"],
    ["https://images.pexels.com/photos/1191531/pexels-photo-1191531.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/691046/pexels-photo-691046.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/10478906/pexels-photo-10478906.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/10478867/pexels-photo-10478867.jpeg?auto=compress&w=800"],
    ["https://images.pexels.com/photos/10478906/pexels-photo-10478906.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/10478867/pexels-photo-10478867.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/691046/pexels-photo-691046.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/1191531/pexels-photo-1191531.jpeg?auto=compress&w=800"],
    ["https://images.pexels.com/photos/1721932/pexels-photo-1721932.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/10478867/pexels-photo-10478867.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/10478906/pexels-photo-10478906.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/691046/pexels-photo-691046.jpeg?auto=compress&w=800"],
]

SILVER_IMG_SETS = [
    ["https://images.pexels.com/photos/8100784/pexels-photo-8100784.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/3266700/pexels-photo-3266700.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/1395306/pexels-photo-1395306.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/2735970/pexels-photo-2735970.jpeg?auto=compress&w=800"],
    ["https://images.pexels.com/photos/3266700/pexels-photo-3266700.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/8100784/pexels-photo-8100784.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/2735970/pexels-photo-2735970.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/1395306/pexels-photo-1395306.jpeg?auto=compress&w=800"],
    ["https://images.pexels.com/photos/1395306/pexels-photo-1395306.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/2735970/pexels-photo-2735970.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/8100784/pexels-photo-8100784.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/3266700/pexels-photo-3266700.jpeg?auto=compress&w=800"],
    ["https://images.pexels.com/photos/2735970/pexels-photo-2735970.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/1395306/pexels-photo-1395306.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/3266700/pexels-photo-3266700.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/8100784/pexels-photo-8100784.jpeg?auto=compress&w=800"],
    ["https://images.pexels.com/photos/8100784/pexels-photo-8100784.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/1395306/pexels-photo-1395306.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/8100784/pexels-photo-8100784.jpeg?auto=compress&w=800",
     "https://images.pexels.com/photos/2735970/pexels-photo-2735970.jpeg?auto=compress&w=800"],
]

gold_products = [
  {"id":"g1","name":"Lakshmi Temple Necklace","category":"Necklace","badge":"Bestseller","weight":"28.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹1,78,500","making":"₹4,200","desc":"Exquisite temple-style necklace featuring Goddess Lakshmi motif with intricate filigree work. Perfect for weddings and poojas. Each piece is handcrafted by master artisans and carries the BIS 916 hallmark guaranteeing genuine 22 karat gold purity.","features":["Handcrafted Temple Design","BIS 916 Hallmark Certified","22 Karat Gold","Lifetime Buyback Available","Free Cleaning & Polishing"]},
  {"id":"g2","name":"Diamond-Cut Mango Haar","category":"Necklace","badge":"New","weight":"35.2g","karat":"22K","purity":"916 BIS Hallmark","price":"₹2,20,400","making":"₹5,500","desc":"Traditional mango (keri) design haar with diamond-cut finish. Radiates elegance at every ceremony and family occasion. The diamond-cut technique creates brilliant light reflection from every angle.","features":["Diamond-Cut Finish","Mango (Keri) Motif","BIS 916 Hallmark","22 Karat Gold","Buyback Policy"]},
  {"id":"g3","name":"Kundan Bridal Set Necklace","category":"Necklace","badge":"Hot","weight":"42.0g","karat":"22K","purity":"916 BIS Hallmark","price":"₹2,63,200","making":"₹6,800","desc":"Royal Kundan-set necklace with meenakari enamelling. Ideal for bridal trousseau and festive occasions. This magnificent piece features hand-set Kundan stones and vibrant enamel work that is characteristic of royal Rajasthani craftsmanship.","features":["Kundan Stone Setting","Meenakari Enamel Work","BIS 916 Hallmark","Bridal Favourite","Royal Craftsmanship"]},
  {"id":"g4","name":"Elegant Solitaire Ring","category":"Ring","badge":"","weight":"4.8g","karat":"18K","purity":"750 Hallmark","price":"₹30,100","making":"₹1,200","desc":"Classic four-prong solitaire ring crafted in 18K gold. Timeless design that suits everyday wear and special occasions. The clean lines and refined silhouette make this a versatile piece for any wardrobe.","features":["Four-Prong Setting","18 Karat Gold","750 Hallmark","Everyday Wear","Timeless Design"]},
  {"id":"g5","name":"Floral Cluster Ring","category":"Ring","badge":"New","weight":"5.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹34,500","making":"₹1,400","desc":"Beautiful floral cluster design ring with textured petals. Great for engagements and anniversaries. Each petal is individually crafted to create a stunning blooming flower effect on your finger.","features":["Floral Cluster Design","Textured Petals","22 Karat Gold","Engagement Ready","BIS Hallmark"]},
  {"id":"g6","name":"Jhumka Earrings Classic","category":"Earring","badge":"Bestseller","weight":"9.2g","karat":"22K","purity":"916 BIS Hallmark","price":"₹57,700","making":"₹2,200","desc":"Traditional gold jhumka with beaded chain danglers. A timeless favourite worn across generations with ethnic outfits. The bell-shaped body and intricate bead-work make these jhumkas a celebration of Indian jewellery tradition.","features":["Traditional Jhumka Style","Beaded Danglers","22 Karat Gold","Lightweight Design","BIS 916 Hallmark"]},
  {"id":"g7","name":"Peacock Bali Earrings","category":"Earring","badge":"","weight":"7.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹47,000","making":"₹1,800","desc":"Peacock-inspired bali earrings with intricate feather detailing. Perfect for sarees and lehengas. The peacock — a symbol of grace and beauty — is rendered in exquisite detail by skilled artisans.","features":["Peacock Motif","Intricate Feather Detail","22 Karat Gold","Ethnic Wear","BIS Hallmark"]},
  {"id":"g8","name":"Plain Kadas Bangles Pair","category":"Bangle","badge":"","weight":"22.0g","karat":"22K","purity":"916 BIS Hallmark","price":"₹1,37,800","making":"₹3,200","desc":"Smooth plain kadas bangles — the epitome of classic simplicity. A must-have in every jewellery collection. The high-polish finish gives these kadas a brilliant mirror-like shine.","features":["High-Polish Finish","Smooth Plain Design","22 Karat Gold","Pair of 2","BIS 916 Hallmark"]},
  {"id":"g9","name":"Antique Kada Set","category":"Bangle","badge":"Hot","weight":"32.4g","karat":"22K","purity":"916 BIS Hallmark","price":"₹2,03,100","making":"₹4,800","desc":"Antique finish kadas with engraved floral motifs. Polished on inside, matte antique exterior — artisan craftsmanship at its finest.","features":["Antique Finish","Engraved Floral Motifs","Polished Interior","22 Karat Gold","BIS Hallmark"]},
  {"id":"g10","name":"Twisted Rope Bracelet","category":"Bracelet","badge":"New","weight":"8.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹53,300","making":"₹1,800","desc":"Elegant twisted rope-pattern gold bracelet with box clasp. Lightweight yet sturdy for daily wear. The rope twist pattern is achieved through a precise hand-twisting technique that creates beautiful texture.","features":["Twisted Rope Pattern","Box Clasp","Daily Wear","22 Karat Gold","BIS Hallmark"]},
  {"id":"g11","name":"Ganesh Pendant","category":"Pendant","badge":"Bestseller","weight":"3.2g","karat":"22K","purity":"916 BIS Hallmark","price":"₹20,100","making":"₹900","desc":"Lord Ganesha pendant with fine detailing. Auspicious and elegant, suitable for daily devotional wear. The remover of obstacles is depicted in fine detail with a seated pose and traditional attributes.","features":["Lord Ganesha Motif","Fine Detailing","22 Karat Gold","Devotional Wear","BIS Hallmark"]},
  {"id":"g12","name":"Heart Locket Pendant","category":"Pendant","badge":"","weight":"2.8g","karat":"18K","purity":"750 Hallmark","price":"₹17,600","making":"₹800","desc":"Romantic heart-shaped locket pendant, ideal as a gift for loved ones on birthdays and anniversaries. Opens to hold a tiny photo or keepsake inside.","features":["Opens as Locket","Heart Shape","18 Karat Gold","Perfect Gift","750 Hallmark"]},
  {"id":"g13","name":"Singapore Chain 22\"","category":"Chain","badge":"","weight":"6.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹40,800","making":"₹1,100","desc":"Classic Singapore chain with machine-cut precision links. Lightweight and perfect for pendants or standalone wear. The interlocking pattern creates flexible, fluid movement.","features":["Machine-Cut Links","22\" Length","Pendant Ready","22 Karat Gold","BIS Hallmark"]},
  {"id":"g14","name":"Figaro Link Chain 24\"","category":"Chain","badge":"New","weight":"9.2g","karat":"22K","purity":"916 BIS Hallmark","price":"₹57,700","making":"₹1,500","desc":"Bold Figaro link chain design. Masculine and feminine both — versatile for all occasions. Features the classic 3-small-1-large link pattern of Italian origin.","features":["Figaro Link Pattern","24\" Length","Unisex Design","22 Karat Gold","BIS Hallmark"]},
  {"id":"g15","name":"Gold Payal with Bells","category":"Anklet","badge":"","weight":"15.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹97,200","making":"₹2,800","desc":"Traditional gold payal/anklet with hanging bells. Auspicious sound and beautiful design for brides and festivals. The ghungroo bells produce a melodious sound with every step.","features":["Ghungroo Bells","Traditional Payal","22 Karat Gold","Bridal Wear","BIS Hallmark"]},
  {"id":"g16","name":"Choker Necklace Meenakari","category":"Necklace","badge":"Hot","weight":"24.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹1,53,600","making":"₹5,000","desc":"Stunning choker necklace with blue and red meenakari enamel work. Bridal favourite across Maharashtra. The vibrant colours are fired into the gold using traditional kiln techniques.","features":["Meenakari Enamel","Choker Style","Bridal Favourite","22 Karat Gold","BIS Hallmark"]},
  {"id":"g17","name":"Mangalsutra 18\"","category":"Necklace","badge":"Bestseller","weight":"8.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹53,300","making":"₹1,600","desc":"Traditional mangalsutra with black bead chain and gold pendant. Essential bridal jewellery symbolising marital status and the sacred bond between husband and wife.","features":["Black Bead Chain","Gold Pendant","18\" Length","22 Karat Gold","Traditional Design"]},
  {"id":"g18","name":"Navratna Finger Ring","category":"Ring","badge":"","weight":"6.2g","karat":"22K","purity":"916 BIS Hallmark","price":"₹38,900","making":"₹1,500","desc":"Nine gemstone navratna ring for astrological benefits. Includes ruby, pearl, coral, emerald, yellow sapphire, blue sapphire, diamond, cat's eye, hessonite — each representing a planet.","features":["9 Gemstones","Astrological Benefits","22 Karat Gold","BIS Hallmark","Planetary Representation"]},
  {"id":"g19","name":"Chandbali Earrings","category":"Earring","badge":"New","weight":"11.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹72,100","making":"₹2,800","desc":"Traditional chandbali (moon-shaped) earrings with pearl drops. Stunning for weddings and receptions. The crescent moon shape is embellished with delicate filigree and hanging pearl drops.","features":["Moon (Chand) Shape","Pearl Drops","Filigree Work","22 Karat Gold","BIS Hallmark"]},
  {"id":"g20","name":"Gold Nose Ring (Nath)","category":"Earring","badge":"","weight":"2.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹15,700","making":"₹700","desc":"Elegant bridal nath with pearl and ruby accents. Traditional Maharashtrian bridal jewellery that adds a touch of regal grace to the bride's look.","features":["Pearl & Ruby Accents","Maharashtrian Style","Bridal Nath","22 Karat Gold","BIS Hallmark"]},
  {"id":"g21","name":"Coin Necklace Set","category":"Necklace","badge":"","weight":"30.0g","karat":"22K","purity":"916 BIS Hallmark","price":"₹1,88,000","making":"₹4,500","desc":"Multi-layer coin necklace with goddess Lakshmi coins. Symbol of prosperity and traditional craftsmanship.","features":["Lakshmi Coin Design","Multi-Layer","Symbol of Prosperity","22 Karat Gold","BIS Hallmark"]},
  {"id":"g22","name":"Gokarna Bangle Set (6pcs)","category":"Bangle","badge":"Bestseller","weight":"38.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹2,41,500","making":"₹6,000","desc":"Six-piece gold bangle set in traditional Gokarna style with carved edges. Perfect for festive occasions.","features":["Set of 6 Bangles","Carved Edges","Gokarna Style","22 Karat Gold","BIS Hallmark"]},
  {"id":"g23","name":"Box Link Bracelet","category":"Bracelet","badge":"","weight":"7.2g","karat":"22K","purity":"916 BIS Hallmark","price":"₹45,100","making":"₹1,500","desc":"Sleek box-link bracelet with lobster clasp. Modern minimalist style for professional women.","features":["Box Link Pattern","Lobster Clasp","Modern Design","22 Karat Gold","BIS Hallmark"]},
  {"id":"g24","name":"Om Pendant 22K","category":"Pendant","badge":"","weight":"4.1g","karat":"22K","purity":"916 BIS Hallmark","price":"₹25,700","making":"₹950","desc":"Sacred Om symbol pendant with fine engraving. Spiritual and stylish for everyday devotional wear.","features":["Sacred Om Symbol","Fine Engraving","22 Karat Gold","Daily Wear","BIS Hallmark"]},
  {"id":"g25","name":"Baby Gold Bangle (Infant)","category":"Bangle","badge":"New","weight":"3.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹21,900","making":"₹700","desc":"Delicate gold bangle for newborns and infants. A traditional gifting choice for baby naming ceremonies.","features":["Infant Size","Delicate Design","22 Karat Gold","Baby Ceremony Gift","BIS Hallmark"]},
  {"id":"g26","name":"Lotus Stud Earrings","category":"Earring","badge":"","weight":"2.8g","karat":"22K","purity":"916 BIS Hallmark","price":"₹17,600","making":"₹700","desc":"Delicate lotus flower stud earrings. Simple, elegant and perfect for everyday wear.","features":["Lotus Flower Design","Stud Style","22 Karat Gold","Everyday Wear","BIS Hallmark"]},
  {"id":"g27","name":"Kali Haar Necklace","category":"Necklace","badge":"","weight":"26.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹1,66,100","making":"₹4,000","desc":"Long kali (black bead) haar with gold caps and pendant. Traditional Maharashtrian jewellery staple.","features":["Black Bead Haar","Gold Caps","Long Style","22 Karat Gold","BIS Hallmark"]},
  {"id":"g28","name":"Designer Toe Rings (Pair)","category":"Ring","badge":"","weight":"2.0g","karat":"22K","purity":"916 BIS Hallmark","price":"₹12,500","making":"₹500","desc":"Traditional toe rings (bichhiya) with floral design. Auspicious for married women and brides.","features":["Floral Design","Pair of 2","Bichhiya Style","22 Karat Gold","BIS Hallmark"]},
  {"id":"g29","name":"Gold Tikka Maang","category":"Necklace","badge":"Hot","weight":"7.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹47,000","making":"₹1,800","desc":"Stunning gold maang tikka with peacock motif and hanging pearls. Ideal bridal head jewellery.","features":["Peacock Motif","Hanging Pearls","Maang Tikka","22 Karat Gold","BIS Hallmark"]},
  {"id":"g30","name":"Curb Link Chain 20\"","category":"Chain","badge":"","weight":"7.8g","karat":"22K","purity":"916 BIS Hallmark","price":"₹48,900","making":"₹1,300","desc":"Heavy curb link chain with excellent lustre. Suitable for men and women who love bold jewellery.","features":["Curb Link Pattern","20\" Length","Bold Style","22 Karat Gold","BIS Hallmark"]},
  {"id":"g31","name":"Hoop Bali Earrings","category":"Earring","badge":"","weight":"5.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹34,500","making":"₹1,200","desc":"Classic gold hoop bali earrings with click closure. Versatile and comfortable for daily wear.","features":["Hoop Design","Click Closure","Daily Wear","22 Karat Gold","BIS Hallmark"]},
  {"id":"g32","name":"Bridal Haath Phool","category":"Bracelet","badge":"Hot","weight":"18.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹1,16,000","making":"₹3,500","desc":"Traditional haath phool (hand flower bracelet) with ring and chain. Essential bridal accessory for henna ceremonies.","features":["Ring + Chain Design","Haath Phool Style","Bridal Accessory","22 Karat Gold","BIS Hallmark"]},
  {"id":"g33","name":"Gold Mathapatti","category":"Necklace","badge":"New","weight":"22.0g","karat":"22K","purity":"916 BIS Hallmark","price":"₹1,37,800","making":"₹4,200","desc":"Elaborate bridal mathapatti (forehead ornament) with floral chains. Unique Maharashtrian bridal tradition.","features":["Mathapatti Design","Floral Chains","Maharashtrian Bridal","22 Karat Gold","BIS Hallmark"]},
  {"id":"g34","name":"Antique Jhumki Drop","category":"Earring","badge":"Bestseller","weight":"10.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹65,800","making":"₹2,500","desc":"Antique-finish jhumki with ruby and emerald accents. Heritage craftsmanship for contemporary brides.","features":["Antique Finish","Ruby & Emerald Accents","Heritage Design","22 Karat Gold","BIS Hallmark"]},
  {"id":"g35","name":"Diamond Bar Ring","category":"Ring","badge":"","weight":"3.5g","karat":"18K","purity":"750 Hallmark","price":"₹21,900","making":"₹1,000","desc":"Minimalist gold bar ring — sleek and modern. Stackable with other rings for a trendy look.","features":["Bar Design","Stackable","Modern Style","18 Karat Gold","750 Hallmark"]},
  {"id":"g36","name":"Polki Set Necklace","category":"Necklace","badge":"Hot","weight":"45.0g","karat":"22K","purity":"916 BIS Hallmark","price":"₹2,82,200","making":"₹8,000","desc":"Royal polki diamond uncut necklace set. Mughal-inspired artistry for weddings and grand ceremonies.","features":["Polki Diamonds","Uncut Stones","Mughal Design","22 Karat Gold","BIS Hallmark"]},
  {"id":"g37","name":"Lakshmi Coin Pendant","category":"Pendant","badge":"","weight":"5.0g","karat":"22K","purity":"916 BIS Hallmark","price":"₹31,300","making":"₹1,100","desc":"Embossed Lakshmi coin pendant — auspicious and elegant for daily wear and gifting.","features":["Lakshmi Embossed","Coin Shape","Daily Wear","22 Karat Gold","BIS Hallmark"]},
  {"id":"g38","name":"Broad Herringbone Chain","category":"Chain","badge":"New","weight":"12.0g","karat":"22K","purity":"916 BIS Hallmark","price":"₹75,200","making":"₹2,000","desc":"Flat herringbone chain with silky smooth texture. A statement piece for confident women.","features":["Herringbone Pattern","Flat Design","Statement Piece","22 Karat Gold","BIS Hallmark"]},
  {"id":"g39","name":"Gold Anklet with Ghungroo","category":"Anklet","badge":"Bestseller","weight":"20.0g","karat":"22K","purity":"916 BIS Hallmark","price":"₹1,25,400","making":"₹3,500","desc":"Ornate gold anklet with ghungroo bells and chain detail. Melodious and mesmerising — a bridal staple.","features":["Ghungroo Bells","Ornate Design","Bridal Staple","22 Karat Gold","BIS Hallmark"]},
  {"id":"g40","name":"Patta Bracelet Wide","category":"Bracelet","badge":"","weight":"14.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹90,900","making":"₹2,800","desc":"Wide flat patta (plate) bracelet with engraved floral border. A bold statement piece.","features":["Wide Plate Design","Engraved Border","Bold Style","22 Karat Gold","BIS Hallmark"]},
  {"id":"g41","name":"Tri-Tone Gold Ring","category":"Ring","badge":"New","weight":"5.8g","karat":"18K","purity":"750 Hallmark","price":"₹36,400","making":"₹1,300","desc":"Three-tone gold ring combining yellow, white and rose gold in a wave design. Modern and fashionable.","features":["Tri-Tone Design","Yellow + White + Rose","Wave Pattern","18 Karat Gold","750 Hallmark"]},
  {"id":"g42","name":"Filigree Drop Earrings","category":"Earring","badge":"","weight":"6.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹40,800","making":"₹1,800","desc":"Handcrafted filigree work drop earrings with intricate wire patterns. Showcases goldsmith artistry.","features":["Handcrafted Filigree","Wire Patterns","Artisan Work","22 Karat Gold","BIS Hallmark"]},
  {"id":"g43","name":"Lotus Pendant Necklace","category":"Pendant","badge":"","weight":"3.8g","karat":"22K","purity":"916 BIS Hallmark","price":"₹23,800","making":"₹900","desc":"Blooming lotus pendant — symbol of purity and grace. Beautiful with both ethnic and western attire.","features":["Lotus Symbol","Blooming Design","Versatile Wear","22 Karat Gold","BIS Hallmark"]},
  {"id":"g44","name":"Italian Wheat Chain 22\"","category":"Chain","badge":"","weight":"8.0g","karat":"22K","purity":"916 BIS Hallmark","price":"₹50,200","making":"₹1,400","desc":"Elegant Italian wheat (spiga) chain with smooth texture. Lightweight and suitable for pendants.","features":["Wheat Link Pattern","22\" Length","Italian Style","22 Karat Gold","BIS Hallmark"]},
  {"id":"g45","name":"Kundan Maang Tikka","category":"Necklace","badge":"Hot","weight":"9.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹59,600","making":"₹2,000","desc":"Kundan set maang tikka with pearl drops. Stunning centrepiece for bridal and festive looks.","features":["Kundan Setting","Pearl Drops","Maang Tikka","22 Karat Gold","BIS Hallmark"]},
  {"id":"g46","name":"Kids Finger Ring","category":"Ring","badge":"New","weight":"1.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹9,400","making":"₹400","desc":"Cute floral design finger ring for children. Perfect gifting for birthdays and baby ceremonies.","features":["Children's Size","Floral Design","Safe for Kids","22 Karat Gold","BIS Hallmark"]},
  {"id":"g47","name":"Gold Ear Chain Sahara","category":"Earring","badge":"","weight":"4.2g","karat":"22K","purity":"916 BIS Hallmark","price":"₹26,300","making":"₹1,000","desc":"Delicate ear chain connecting stud to top of ear. Trendy and distinctive Bollywood-inspired look.","features":["Ear Chain Design","Stud to Top","Trendy Style","22 Karat Gold","BIS Hallmark"]},
  {"id":"g48","name":"Bajuband Armlet","category":"Bracelet","badge":"Bestseller","weight":"16.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹1,03,500","making":"₹3,200","desc":"Traditional bajuband (armlet) with adjustable chain. Bridal upper-arm jewellery crafted to perfection.","features":["Bajuband Style","Adjustable Chain","Upper Arm Wear","22 Karat Gold","BIS Hallmark"]},
  {"id":"g49","name":"Half-Bangle Cuff","category":"Bangle","badge":"","weight":"12.0g","karat":"22K","purity":"916 BIS Hallmark","price":"₹75,200","making":"₹2,400","desc":"Open-end cuff bangle with geometric diamond-cut pattern. Contemporary look with traditional gold purity.","features":["Open Cuff Design","Diamond-Cut Pattern","Contemporary Style","22 Karat Gold","BIS Hallmark"]},
  {"id":"g50","name":"Five Petal Flower Anklet","category":"Anklet","badge":"New","weight":"12.5g","karat":"22K","purity":"916 BIS Hallmark","price":"₹78,400","making":"₹2,500","desc":"Delicate flower charm anklet with bell drops. Feminine and elegant for festive occasions and weddings.","features":["Flower Charms","Bell Drops","Feminine Design","22 Karat Gold","BIS Hallmark"]},
]

silver_products = [
  {"id":"s1","name":"Silver Kundan Necklace Set","category":"Necklace","badge":"Bestseller","weight":"62g","purity":"925 Sterling","finish":"Rhodium","price":"₹4,850","making":"₹350","desc":"Stunning silver kundan necklace with earring set. Perfect for festivals and ethnic occasions. The rhodium finish gives a brilliant white-gold appearance while maintaining affordability.","features":["Kundan Setting","Rhodium Finish","Set with Earrings","925 Sterling Silver","Anti-Tarnish"]},
  {"id":"s2","name":"Oxidised Collar Necklace","category":"Necklace","badge":"New","weight":"48g","purity":"925 Sterling","finish":"Oxidised","price":"₹3,200","making":"₹250","desc":"Bold oxidised silver collar necklace with tribal motifs. Boho-chic style for statement looks.","features":["Oxidised Finish","Collar Style","Tribal Motifs","925 Sterling Silver","Boho Design"]},
  {"id":"s3","name":"Silver Temple Choker","category":"Necklace","badge":"","weight":"55g","purity":"925 Sterling","finish":"Polished","price":"₹4,200","making":"₹320","desc":"South Indian temple-style choker with Goddess Lakshmi motif. Traditional craftsmanship in fine silver.","features":["Temple Design","Lakshmi Motif","Choker Style","925 Sterling Silver","Polished Finish"]},
  {"id":"s4","name":"Silver Filigree Ring","category":"Ring","badge":"","weight":"5g","purity":"925 Sterling","finish":"Polished","price":"₹680","making":"₹80","desc":"Delicate filigree-work silver ring with intricate wire patterns. A timeless artisan piece.","features":["Filigree Work","Wire Patterns","Artisan Made","925 Sterling Silver","Polished Finish"]},
  {"id":"s5","name":"Turquoise Stone Ring","category":"Ring","badge":"Hot","weight":"7g","purity":"925 Sterling","finish":"Oxidised","price":"₹950","making":"₹100","desc":"Natural turquoise cabochon set in 925 silver. Beautiful sky-blue stone ring for boho style lovers.","features":["Natural Turquoise","Cabochon Setting","Oxidised Finish","925 Sterling Silver","Boho Style"]},
  {"id":"s6","name":"Silver Jhumka Classic","category":"Earring","badge":"Bestseller","weight":"18g","purity":"925 Sterling","finish":"Polished","price":"₹1,450","making":"₹180","desc":"Traditional silver jhumka earrings — a must-have in every Indian woman's jewellery box.","features":["Classic Jhumka","Bell Shape","925 Sterling Silver","Traditional Design","Polished Finish"]},
  {"id":"s7","name":"Oxidised Chandbali","category":"Earring","badge":"New","weight":"22g","purity":"925 Sterling","finish":"Oxidised","price":"₹1,750","making":"₹200","desc":"Oxidised silver chandbali earrings with turquoise and red coral beads. Festival favourite.","features":["Chandbali Shape","Turquoise & Coral Beads","Oxidised Finish","925 Sterling Silver","Festival Wear"]},
  {"id":"s8","name":"Silver Bangle Pair Plain","category":"Bangle","badge":"","weight":"50g","purity":"92.5%","finish":"Polished","price":"₹3,800","making":"₹280","desc":"Classic plain silver bangles — timeless simplicity. Anti-tarnish coating for lasting shine.","features":["Plain Design","Anti-Tarnish Coating","925 Silver","Pair of 2","Polished Finish"]},
  {"id":"s9","name":"Floral Engraved Bangle","category":"Bangle","badge":"Bestseller","weight":"65g","purity":"925 Sterling","finish":"Polished","price":"₹4,950","making":"₹380","desc":"Flower-engraved wide silver bangle with matte interior finish. Elegant for daily or occasional wear.","features":["Floral Engraving","Wide Design","Matte Interior","925 Sterling Silver","Polished Exterior"]},
  {"id":"s10","name":"Silver Charm Bracelet","category":"Bracelet","badge":"New","weight":"15g","purity":"925 Sterling","finish":"Polished","price":"₹1,850","making":"₹180","desc":"Silver charm bracelet with 8 traditional Indian charms including lotus, peacock and elephant.","features":["8 Indian Charms","Lotus, Peacock, Elephant","925 Sterling Silver","Polished Finish","Lobster Clasp"]},
  {"id":"s11","name":"Ganesh Silver Pendant","category":"Pendant","badge":"Bestseller","weight":"8g","purity":"925 Sterling","finish":"Polished","price":"₹920","making":"₹90","desc":"Lord Ganesha pendant in 925 silver. Auspicious, detailed and perfect for daily devotional wear.","features":["Lord Ganesha","Detailed Carving","Daily Wear","925 Sterling Silver","Polished Finish"]},
  {"id":"s12","name":"Star Pendant Silver","category":"Pendant","badge":"","weight":"5g","purity":"925 Sterling","finish":"Polished","price":"₹580","making":"₹70","desc":"Simple five-pointed star pendant. Minimalist design for casual everyday wear.","features":["Star Design","Minimalist","Five Points","925 Sterling Silver","Polished Finish"]},
  {"id":"s13","name":"Silver Payal (Pair)","category":"Payal","badge":"Bestseller","weight":"40g","purity":"925 Sterling","finish":"Polished","price":"₹3,050","making":"₹250","desc":"Traditional silver payal with ghungroo bells. Melodious and beautiful anklets for all ages.","features":["Ghungroo Bells","Pair of 2","Traditional Design","925 Sterling Silver","Melodious Sound"]},
  {"id":"s14","name":"Beaded Silver Payal","category":"Payal","badge":"New","weight":"35g","purity":"925 Sterling","finish":"Polished","price":"₹2,650","making":"₹220","desc":"Silver payal with coral and turquoise beads. Tribal-inspired design perfect for festive looks.","features":["Coral & Turquoise Beads","Tribal Design","Pair of 2","925 Sterling Silver","Festive Wear"]},
  {"id":"s15","name":"Lakshmi Silver Idol (6\")","category":"Idol","badge":"","weight":"250g","purity":"999 Fine Silver","finish":"Polished","price":"₹19,200","making":"₹1,500","desc":"Beautifully crafted seated Goddess Lakshmi idol in fine silver. Ideal for pooja, housewarming and gifting.","features":["Seated Lakshmi","6 Inch Height","999 Fine Silver","Pooja Ready","Gift Box Included"]},
  {"id":"s16","name":"Silver Kada Pair","category":"Bangle","badge":"Hot","weight":"80g","purity":"925 Sterling","finish":"Polished","price":"₹6,100","making":"₹450","desc":"Heavy silver kadas with carved border. Traditional and sturdy for every day or religious occasions.","features":["Carved Border","Heavy Weight","Pair of 2","925 Sterling Silver","Polished Finish"]},
  {"id":"s17","name":"Silver Hoop Earrings Large","category":"Earring","badge":"","weight":"10g","purity":"925 Sterling","finish":"Polished","price":"₹800","making":"₹90","desc":"Large classic silver hoop earrings. Effortlessly stylish for both casual and party looks.","features":["Large Hoops","Click Closure","925 Sterling Silver","Versatile Style","Polished Finish"]},
  {"id":"s18","name":"Ganapati Silver Coin","category":"Idol","badge":"New","weight":"50g","purity":"999 Fine Silver","finish":"Polished","price":"₹3,850","making":"₹300","desc":"999 pure silver Ganesha coin — perfect Dhanteras and Diwali gift for prosperity and blessings.","features":["Ganesha Motif","999 Fine Silver","Diwali Gift","50g Weight","Gift Box Included"]},
  {"id":"s19","name":"Silver Cuff Bracelet","category":"Bracelet","badge":"Hot","weight":"28g","purity":"925 Sterling","finish":"Oxidised","price":"₹2,150","making":"₹200","desc":"Bold oxidised cuff bracelet with tribal motifs. Statement piece for boho and ethnic style.","features":["Cuff Style","Tribal Motifs","Oxidised Finish","925 Sterling Silver","Statement Piece"]},
  {"id":"s20","name":"Peacock Pendant Silver","category":"Pendant","badge":"","weight":"10g","purity":"925 Sterling","finish":"Oxidised","price":"₹1,150","making":"₹120","desc":"Detailed peacock pendant with spread feathers and coloured enamel accents. Elegant and artistic.","features":["Peacock Design","Spread Feathers","Enamel Accents","925 Sterling Silver","Oxidised Finish"]},
  {"id":"s21","name":"Silver Navratan Necklace","category":"Necklace","badge":"Bestseller","weight":"58g","purity":"925 Sterling","finish":"Polished","price":"₹5,200","making":"₹400","desc":"Nine-gemstone silver necklace combining traditional healing stones in elegant silver setting.","features":["9 Gemstones","Healing Stones","925 Sterling Silver","Traditional Design","Polished Finish"]},
  {"id":"s22","name":"Silver Toe Rings Pair","category":"Ring","badge":"","weight":"4g","purity":"925 Sterling","finish":"Polished","price":"₹310","making":"₹50","desc":"Classic silver toe rings (bichhiya) in floral design. Auspicious for married women.","features":["Floral Design","Pair of 2","Bichhiya Style","925 Sterling Silver","Auspicious"]},
  {"id":"s23","name":"Shiva Linga Silver Idol","category":"Idol","badge":"","weight":"150g","purity":"999 Fine Silver","finish":"Polished","price":"₹11,550","making":"₹900","desc":"Sacred Shiva Linga in fine 999 silver. A powerful pooja item for devotees of Lord Shiva.","features":["Shiva Linga","999 Fine Silver","Sacred Item","Pooja Ready","Gift Wrapped"]},
  {"id":"s24","name":"Silver Mangalsutra Pendant","category":"Pendant","badge":"New","weight":"9g","purity":"925 Sterling","finish":"Polished","price":"₹1,040","making":"₹110","desc":"Modern silver mangalsutra pendant — a contemporary take on a beloved traditional ornament.","features":["Modern Design","Mangalsutra Style","925 Sterling Silver","Polished Finish","Contemporary"]},
  {"id":"s25","name":"Silver Pooja Thali Set","category":"Idol","badge":"Hot","weight":"400g","purity":"999 Fine Silver","finish":"Polished","price":"₹30,800","making":"₹2,500","desc":"Complete silver pooja thali set with diya, kalash and incense holder. Premium gifting choice.","features":["Complete Thali Set","Diya + Kalash","999 Fine Silver","Premium Gift","Box Included"]},
  {"id":"s26","name":"Silver Stud Earrings Ball","category":"Earring","badge":"","weight":"3g","purity":"925 Sterling","finish":"Polished","price":"₹240","making":"₹40","desc":"Simple round ball stud earrings. Everyday essential that goes with any outfit.","features":["Ball Studs","Push Back","925 Sterling Silver","Everyday Wear","Polished Finish"]},
  {"id":"s27","name":"Oxidised Jhumka Cluster","category":"Earring","badge":"Bestseller","weight":"25g","purity":"925 Sterling","finish":"Oxidised","price":"₹1,950","making":"₹220","desc":"Large cluster oxidised jhumka with multicolour bead drops. Bold statement ethnic earrings.","features":["Cluster Design","Multicolour Beads","Oxidised Finish","925 Sterling Silver","Statement Earrings"]},
  {"id":"s28","name":"Silver Chain 20\" Thin","category":"Necklace","badge":"","weight":"8g","purity":"925 Sterling","finish":"Polished","price":"₹620","making":"₹70","desc":"Thin delicate silver chain — ideal for pendants and layering. Lightweight for daily wear.","features":["Thin Design","20\" Length","Pendant Ready","925 Sterling Silver","Layering Chain"]},
  {"id":"s29","name":"Silver Adjustable Ring","category":"Ring","badge":"New","weight":"6g","purity":"925 Sterling","finish":"Polished","price":"₹810","making":"₹85","desc":"Open-band adjustable silver ring — fits all sizes. Ideal for gifting without knowing ring size.","features":["Adjustable Size","Open Band","Fits All","925 Sterling Silver","Gift Friendly"]},
  {"id":"s30","name":"Silver Coin Laxmi-Ganesh","category":"Idol","badge":"Bestseller","weight":"100g","purity":"999 Fine Silver","finish":"Polished","price":"₹7,700","making":"₹600","desc":"Combined Laxmi-Ganesh silver coin — the ultimate Diwali gift for businesses and families.","features":["Laxmi-Ganesh","Combined Coin","999 Fine Silver","Diwali Gift","100g Weight"]},
  {"id":"s31","name":"Silver Ear Cuff Set","category":"Earring","badge":"","weight":"6g","purity":"925 Sterling","finish":"Polished","price":"₹480","making":"₹60","desc":"Trendy ear cuff set — no piercing needed. Modern minimalist design for fashion-forward buyers.","features":["No Piercing Needed","Ear Cuff","Modern Style","925 Sterling Silver","Set of 2"]},
  {"id":"s32","name":"Silver Oxidised Nath","category":"Necklace","badge":"","weight":"12g","purity":"925 Sterling","finish":"Oxidised","price":"₹950","making":"₹100","desc":"Traditional oxidised silver nose ring (nath) with chain. Stunning for brides and festive looks.","features":["Nath Style","With Chain","Oxidised Finish","925 Sterling Silver","Bridal Wear"]},
  {"id":"s33","name":"Silver Bracelet Kids","category":"Bracelet","badge":"New","weight":"8g","purity":"925 Sterling","finish":"Polished","price":"₹620","making":"₹70","desc":"Cute hearts-and-flowers silver bracelet for children. Perfect baby shower or birthday gift.","features":["Kids Size","Hearts & Flowers","925 Sterling Silver","Gift Ready","Safe Design"]},
  {"id":"s34","name":"Balaji Silver Idol (4\")","category":"Idol","badge":"","weight":"180g","purity":"999 Fine Silver","finish":"Polished","price":"₹13,860","making":"₹1,100","desc":"Lord Venkateswara (Balaji) idol in fine silver. Sacred idol for home mandir and gifting.","features":["Balaji / Venkateswara","4 Inch Height","999 Fine Silver","Mandir Ready","Gift Box"]},
  {"id":"s35","name":"Silver Om Pendant","category":"Pendant","badge":"","weight":"7g","purity":"925 Sterling","finish":"Polished","price":"₹810","making":"₹85","desc":"Sacred Om pendant in 925 silver with polished shine. Wearable spirituality for daily use.","features":["Om Symbol","Sacred Design","925 Sterling Silver","Daily Wear","Polished Finish"]},
  {"id":"s36","name":"Silver Maang Tikka","category":"Necklace","badge":"Hot","weight":"14g","purity":"925 Sterling","finish":"Polished","price":"₹1,080","making":"₹120","desc":"Classic silver maang tikka with drop pearl. Completes bridal and festive looks beautifully.","features":["Pearl Drop","Maang Tikka","925 Sterling Silver","Bridal Wear","Polished Finish"]},
  {"id":"s37","name":"Silver Banana Bangle","category":"Bangle","badge":"","weight":"45g","purity":"925 Sterling","finish":"Polished","price":"₹3,465","making":"₹280","desc":"Traditional banana (kela) shaped bangle — a beloved style in Maharashtra and Karnataka.","features":["Banana Shape","Traditional Design","925 Sterling Silver","Maharashtra Style","Polished Finish"]},
  {"id":"s38","name":"Silver Snake Chain 24\"","category":"Necklace","badge":"New","weight":"12g","purity":"925 Sterling","finish":"Polished","price":"₹925","making":"₹95","desc":"Smooth snake chain in 925 silver. A sleek and versatile chain for pendants and solo wear.","features":["Snake Pattern","24\" Length","925 Sterling Silver","Pendant Ready","Smooth Texture"]},
  {"id":"s39","name":"Silver Shankh Figurine","category":"Idol","badge":"","weight":"120g","purity":"999 Fine Silver","finish":"Polished","price":"₹9,240","making":"₹750","desc":"Sacred conch shell (shankh) in fine silver. Used in daily puja rituals and as decor.","features":["Shankh / Conch Shell","999 Fine Silver","Puja Item","Decorative","Gift Ready"]},
  {"id":"s40","name":"Oxidised Hasli Necklace","category":"Necklace","badge":"Bestseller","weight":"70g","purity":"925 Sterling","finish":"Oxidised","price":"₹5,400","making":"₹420","desc":"Bold oxidised hasli (rigid collar) necklace with intricate tribal detailing. A head-turner at any event.","features":["Hasli Design","Rigid Collar","Oxidised Finish","925 Sterling Silver","Tribal Detailing"]},
  {"id":"s41","name":"Silver Infinity Ring","category":"Ring","badge":"","weight":"5g","purity":"925 Sterling","finish":"Polished","price":"₹680","making":"₹75","desc":"Classic infinity symbol ring in polished silver. Symbolises eternal love — a perfect gift.","features":["Infinity Symbol","Eternal Love","925 Sterling Silver","Gift Perfect","Polished Finish"]},
  {"id":"s42","name":"Meenakari Jhumka Silver","category":"Earring","badge":"Hot","weight":"20g","purity":"925 Sterling","finish":"Meenakari","price":"₹1,580","making":"₹170","desc":"Silver jhumka with vibrant blue and red meenakari enamel. Colourful ethnic jewellery at its best.","features":["Meenakari Enamel","Blue & Red Colours","Jhumka Style","925 Sterling Silver","Ethnic Design"]},
  {"id":"s43","name":"Silver Lakshmi Coin Pendant","category":"Pendant","badge":"Bestseller","weight":"12g","purity":"925 Sterling","finish":"Polished","price":"₹1,390","making":"₹130","desc":"Embossed Goddess Lakshmi coin pendant in 925 silver. Auspicious and elegant for daily wear.","features":["Lakshmi Motif","Coin Shape","925 Sterling Silver","Daily Wear","Auspicious"]},
  {"id":"s44","name":"Silver Haath Phool","category":"Bracelet","badge":"New","weight":"32g","purity":"925 Sterling","finish":"Polished","price":"₹2,465","making":"₹230","desc":"Silver haath phool (hand flower) with ring and bracelet. Traditional bridal hand jewellery.","features":["Haath Phool Style","Ring + Bracelet","925 Sterling Silver","Bridal Wear","Traditional"]},
  {"id":"s45","name":"Silver Ganesh Coin 50g","category":"Idol","badge":"","weight":"50g","purity":"999 Fine Silver","finish":"Polished","price":"₹3,850","making":"₹300","desc":"50g Ganesh silver coin. Cherished gifting item for Ganesh Chaturthi, Diwali and business openings.","features":["Ganesh Motif","50g Weight","999 Fine Silver","Festival Gift","Gift Wrapped"]},
  {"id":"s46","name":"Silver Bib Statement Necklace","category":"Necklace","badge":"","weight":"72g","purity":"925 Sterling","finish":"Oxidised","price":"₹5,550","making":"₹430","desc":"Wide bib statement necklace with layered oxidised chains and stone accents. Bold and dramatic.","features":["Bib Design","Layered Chains","Stone Accents","925 Sterling Silver","Statement Piece"]},
  {"id":"s47","name":"Silver Drop Pearl Earrings","category":"Earring","badge":"","weight":"8g","purity":"925 Sterling","finish":"Polished","price":"₹640","making":"₹70","desc":"Simple fresh-water pearl drop earrings in silver. Elegant for office wear and casual occasions.","features":["Fresh-Water Pearl","Drop Style","925 Sterling Silver","Office Wear","Polished Finish"]},
  {"id":"s48","name":"Silver Elephant Charm Payal","category":"Payal","badge":"Hot","weight":"42g","purity":"925 Sterling","finish":"Oxidised","price":"₹3,235","making":"₹260","desc":"Unique payal with elephant charms and oxidised finish. Bohemian style for festivals and beach occasions.","features":["Elephant Charms","Oxidised Finish","925 Sterling Silver","Boho Style","Festival Wear"]},
  {"id":"s49","name":"Silver Gemstone Bracelet","category":"Bracelet","badge":"New","weight":"18g","purity":"925 Sterling","finish":"Polished","price":"₹1,390","making":"₹140","desc":"Silver bracelet with alternating amethyst and garnet stones. Colourful and chic for any occasion.","features":["Amethyst & Garnet","Alternating Stones","925 Sterling Silver","Polished Finish","Colourful Design"]},
  {"id":"s50","name":"Silver Saraswati Idol (5\")","category":"Idol","badge":"Bestseller","weight":"200g","purity":"999 Fine Silver","finish":"Polished","price":"₹15,400","making":"₹1,200","desc":"Goddess Saraswati idol in fine silver with veena. Gifted on Saraswati Puja, Vasant Panchami and housewarmings.","features":["Goddess Saraswati","With Veena","5 Inch Height","999 Fine Silver","Gift Box Included"]},
]

def badge_label(badge):
    if badge == 'Bestseller': return '<span class="badge badge-best">★ Bestseller</span>'
    if badge == 'New': return '<span class="badge badge-new">New Arrival</span>'
    if badge == 'Hot': return '<span class="badge badge-hot">🔥 Hot</span>'
    return ''

def make_page(p, ptype, imgs, prev_id, next_id, all_products):
    is_gold = ptype == 'gold'
    accent = '#C9A84C' if is_gold else '#5A6A7A'
    accent_light = '#E8D48B' if is_gold else '#A8B8C8'
    accent_dark = '#8B6914' if is_gold else '#3A4A5A'
    section_label = 'Gold Jewellery' if is_gold else 'Silver Jewellery'
    section_id = 'gold' if is_gold else 'silver'

    wa_msg = f"Hello Nandgaonkar Jewellers! I am interested in \"{p['name']}\" ({p.get('karat','') + ' ' if is_gold else ''}{p['purity']}) priced at {p['price']}. Please share more details and availability."
    import urllib.parse
    wa_encoded = urllib.parse.quote(wa_msg)

    # specs rows
    if is_gold:
        specs = [
            ("Weight", p['weight']),
            ("Karat", p['karat']),
            ("Purity", p['purity']),
            ("Price", p['price']),
            ("Making Charges", p['making']),
            ("Category", p['category']),
        ]
    else:
        specs = [
            ("Weight", p['weight']),
            ("Purity", p['purity']),
            ("Finish", p['finish']),
            ("Price", p['price']),
            ("Making Charges", p['making']),
            ("Category", p['category']),
        ]

    specs_html = ''.join(f'''
        <div class="spec-row">
          <span class="spec-label">{k}</span>
          <span class="spec-value">{v}</span>
        </div>''' for k,v in specs)

    features_html = ''.join(f'<li>✦ {f}</li>' for f in p.get('features', []))

    thumb_html = ''.join(f'<img class="thumb{" active" if i==0 else ""}" src="{src}" alt="View {i+1}" onclick="setMain(this,\'{src}\')">' for i,src in enumerate(imgs))

    # related products (same category, different id, max 4)
    related = [x for x in all_products if x['category']==p['category'] and x['id']!=p['id']][:4]
    related_html = ''
    for r in related:
        ri = all_products.index(r) % len(GOLD_IMG_SETS if is_gold else SILVER_IMG_SETS)
        rimg = (GOLD_IMG_SETS if is_gold else SILVER_IMG_SETS)[ri][0]
        rwa = urllib.parse.quote(f"Hello! I am interested in \"{r['name']}\" priced at {r['price']}.")
        related_html += f'''
        <a class="rel-card" href="{r['id']}.html">
          <img src="{rimg}" alt="{r['name']}" loading="lazy">
          <div class="rel-body">
            <p class="rel-cat">{r['category']}</p>
            <p class="rel-name">{r['name']}</p>
            <p class="rel-price">{r['price']}</p>
          </div>
        </a>'''

    prev_link = f'<a href="{prev_id}.html" class="nav-arrow">&#8592; Prev</a>' if prev_id else '<span></span>'
    next_link = f'<a href="{next_id}.html" class="nav-arrow">Next &#8594;</a>' if next_id else '<span></span>'

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p['name']} | Nandgaonkar Jewellers</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Cinzel:wght@400;600;700&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<style>
:root{{
  --accent:{accent};
  --accent-light:{accent_light};
  --accent-dark:{accent_dark};
  --black:#0D0D0D;
  --cream:#FAF6EF;
  --white:#FFFFFF;
  --text:#2C2C2C;
  --muted:#7A7A7A;
  --border:#EDEAE3;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{font-family:'Jost',sans-serif;background:var(--cream);color:var(--text);}}

/* NAV */
.top-nav{{
  position:sticky;top:0;z-index:100;
  background:rgba(13,13,13,0.97);backdrop-filter:blur(10px);
  border-bottom:1px solid rgba(201,168,76,0.2);
  display:flex;align-items:center;justify-content:space-between;
  padding:0 40px;height:64px;
}}
.nav-logo{{font-family:'Cinzel',serif;font-size:18px;color:{accent_light};letter-spacing:1px;text-decoration:none;}}
.nav-links{{display:flex;gap:16px;align-items:center;}}
.nav-links a{{color:rgba(255,255,255,0.5);text-decoration:none;font-size:13px;letter-spacing:1.5px;transition:color 0.2s;}}
.nav-links a:hover{{color:var(--accent-light);}}
.nav-links .sep{{color:rgba(255,255,255,0.2);}}
.nav-wa{{
  display:flex;align-items:center;gap:8px;background:#25D366;color:#fff;
  border:none;padding:9px 18px;cursor:pointer;
  font-size:13px;font-family:'Jost',sans-serif;letter-spacing:1px;
  text-decoration:none;transition:all 0.2s;
}}
.nav-wa:hover{{background:#1ea855;}}

/* BREADCRUMB */
.breadcrumb{{
  padding:18px 40px;font-size:12px;letter-spacing:1px;
  color:var(--muted);display:flex;gap:8px;align-items:center;flex-wrap:wrap;
}}
.breadcrumb a{{color:var(--muted);text-decoration:none;transition:color 0.2s;}}
.breadcrumb a:hover{{color:var(--accent);}}
.breadcrumb .sep{{color:var(--border);}}

/* PREV/NEXT */
.prod-nav{{
  display:flex;justify-content:space-between;align-items:center;
  padding:0 40px 14px;
}}
.nav-arrow{{
  font-family:'Jost',sans-serif;font-size:12px;letter-spacing:2px;text-transform:uppercase;
  color:var(--accent);text-decoration:none;
  border-bottom:1px solid var(--accent);padding-bottom:2px;transition:all 0.2s;
}}
.nav-arrow:hover{{color:var(--accent-dark);}}

/* MAIN LAYOUT */
.product-layout{{
  display:grid;grid-template-columns:1fr 1fr;gap:0;
  max-width:1200px;margin:0 auto;padding:0 40px 60px;
}}
@media(max-width:768px){{
  .product-layout{{grid-template-columns:1fr;padding:0 16px 40px;}}
  .top-nav{{padding:0 16px;}}
  .breadcrumb,.prod-nav{{padding-left:16px;padding-right:16px;}}
}}

/* GALLERY */
.gallery{{position:sticky;top:80px;align-self:start;padding-right:40px;}}
@media(max-width:768px){{.gallery{{position:static;padding-right:0;margin-bottom:30px;}}}}
.main-img-wrap{{
  position:relative;background:#F7F5F0;
  width:100%;padding-bottom:100%;overflow:hidden;
}}
.main-img-wrap img{{
  position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  transition:opacity 0.4s ease;
}}
.badge{{
  position:absolute;top:16px;left:16px;z-index:2;
  font-family:'Jost',sans-serif;font-size:11px;letter-spacing:1.5px;
  padding:5px 12px;font-weight:500;
}}
.badge-best{{background:var(--accent);color:#fff;}}
.badge-new{{background:#2C6B2F;color:#fff;}}
.badge-hot{{background:#B22222;color:#fff;}}
.thumbs{{display:flex;gap:10px;margin-top:12px;flex-wrap:wrap;}}
.thumb{{
  width:80px;height:80px;object-fit:cover;cursor:pointer;
  border:2px solid transparent;transition:all 0.2s;opacity:0.7;
}}
.thumb:hover,.thumb.active{{border-color:var(--accent);opacity:1;}}

/* INFO PANEL */
.info-panel{{padding-left:20px;}}
@media(max-width:768px){{.info-panel{{padding-left:0;}}}}
.prod-cat{{
  font-size:11px;letter-spacing:3px;text-transform:uppercase;
  color:var(--accent);margin-bottom:10px;font-family:'Jost',sans-serif;
}}
.prod-name{{
  font-family:'Cinzel',serif;font-size:clamp(1.5rem,3vw,2.2rem);
  font-weight:600;line-height:1.2;margin-bottom:16px;
}}
.prod-price{{
  font-family:'Cinzel',serif;font-size:2rem;
  color:var(--accent-dark);margin-bottom:4px;
}}
.making-note{{font-size:12px;color:var(--muted);margin-bottom:24px;letter-spacing:1px;}}
.divider{{width:60px;height:2px;background:linear-gradient(90deg,var(--accent),transparent);margin-bottom:24px;}}

/* SPECS TABLE */
.specs-table{{margin-bottom:24px;border:1px solid var(--border);}}
.spec-row{{
  display:flex;border-bottom:1px solid var(--border);
}}
.spec-row:last-child{{border-bottom:none;}}
.spec-label{{
  width:140px;min-width:140px;padding:12px 16px;
  font-size:11px;letter-spacing:1.5px;text-transform:uppercase;
  color:var(--muted);background:#F7F5F0;border-right:1px solid var(--border);
}}
.spec-value{{
  padding:12px 16px;font-family:'Cormorant Garamond',serif;
  font-size:1rem;font-weight:600;color:var(--text);flex:1;
}}

/* DESCRIPTION */
.prod-desc{{
  font-family:'Cormorant Garamond',serif;
  font-size:1.08rem;line-height:1.75;color:var(--muted);margin-bottom:24px;
}}

/* FEATURES */
.features-title{{
  font-family:'Cinzel',serif;font-size:13px;letter-spacing:2px;
  text-transform:uppercase;margin-bottom:12px;color:var(--text);
}}
.features-list{{list-style:none;display:flex;flex-direction:column;gap:7px;margin-bottom:28px;}}
.features-list li{{
  font-family:'Jost',sans-serif;font-size:13px;color:var(--muted);
  display:flex;align-items:center;gap:8px;
}}
.features-list li::before{{content:'';width:4px;height:4px;border-radius:50%;background:var(--accent);flex-shrink:0;}}

/* CTA BUTTONS */
.cta-buttons{{display:flex;flex-direction:column;gap:12px;}}
.btn-wa-big{{
  display:flex;align-items:center;justify-content:center;gap:12px;
  background:#25D366;color:#fff;border:none;
  padding:17px;cursor:pointer;text-decoration:none;
  font-family:'Cinzel',serif;font-size:14px;letter-spacing:2px;
  transition:all 0.3s;
}}
.btn-wa-big:hover{{background:#1ea855;transform:translateY(-2px);box-shadow:0 8px 24px rgba(37,211,102,0.4);}}
.btn-back{{
  display:flex;align-items:center;justify-content:center;gap:8px;
  background:transparent;color:var(--accent);
  border:1px solid var(--accent);padding:15px;
  text-decoration:none;font-family:'Cinzel',serif;font-size:13px;letter-spacing:2px;
  transition:all 0.3s;cursor:pointer;
}}
.btn-back:hover{{background:var(--accent);color:#fff;}}

/* TRUST BADGES */
.trust-row{{
  display:flex;flex-wrap:wrap;gap:16px;margin-top:24px;padding-top:24px;
  border-top:1px solid var(--border);
}}
.trust-item{{
  display:flex;align-items:center;gap:8px;
  font-size:11px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;
}}
.trust-icon{{font-size:18px;}}

/* RELATED */
.related-section{{
  max-width:1200px;margin:0 auto;padding:40px 40px 80px;
  border-top:1px solid var(--border);
}}
@media(max-width:768px){{.related-section{{padding:30px 16px 60px;}}}}
.related-title{{
  font-family:'Cinzel',serif;font-size:1.4rem;
  text-align:center;margin-bottom:8px;
}}
.related-sub{{
  font-family:'Cormorant Garamond',serif;font-style:italic;
  color:var(--muted);text-align:center;margin-bottom:30px;
}}
.related-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:20px;}}
.rel-card{{text-decoration:none;color:var(--text);background:#fff;border:1px solid var(--border);transition:all 0.3s;overflow:hidden;}}
.rel-card:hover{{transform:translateY(-4px);box-shadow:0 12px 36px rgba(0,0,0,0.1);border-color:var(--accent);}}
.rel-card img{{width:100%;height:180px;object-fit:cover;}}
.rel-body{{padding:14px;}}
.rel-cat{{font-size:10px;letter-spacing:2px;text-transform:uppercase;color:var(--accent);margin-bottom:4px;}}
.rel-name{{font-family:'Cinzel',serif;font-size:13px;line-height:1.3;margin-bottom:6px;}}
.rel-price{{font-family:'Cinzel',serif;font-size:1rem;color:var(--accent-dark);font-weight:600;}}

/* FOOTER */
footer{{background:#080808;text-align:center;padding:24px;color:rgba(255,255,255,0.3);font-size:12px;letter-spacing:1px;}}
footer span{{color:{accent};}}

/* WA FLOAT */
.wa-float{{
  position:fixed;bottom:28px;right:28px;z-index:200;
  width:56px;height:56px;border-radius:50%;
  background:#25D366;display:flex;align-items:center;justify-content:center;
  box-shadow:0 6px 24px rgba(37,211,102,0.5);
  text-decoration:none;font-size:24px;transition:all 0.3s;
}}
.wa-float:hover{{transform:scale(1.1);}}
</style>
</head>
<body>

<a href="https://wa.me/{PHONE}?text={wa_encoded}" target="_blank" class="wa-float" title="Chat on WhatsApp">💬</a>

<!-- NAV -->
<nav class="top-nav">
  <a href="../index.html" class="nav-logo">✦ Nandgaonkar</a>
  <div class="nav-links">
    <a href="../index.html#{section_id}">← Catalogue</a>
    <span class="sep">|</span>
    <a href="../index.html#gold">Gold</a>
    <span class="sep">|</span>
    <a href="../index.html#silver">Silver</a>
  </div>
  <a href="https://wa.me/{PHONE}?text={wa_encoded}" target="_blank" class="nav-wa">💬 Enquire</a>
</nav>

<!-- BREADCRUMB -->
<div class="breadcrumb">
  <a href="../index.html">Home</a>
  <span class="sep">›</span>
  <a href="../index.html#{section_id}">{section_label}</a>
  <span class="sep">›</span>
  <a href="../index.html#{section_id}">{p['category']}</a>
  <span class="sep">›</span>
  <span>{p['name']}</span>
</div>

<!-- PREV / NEXT -->
<div class="prod-nav">
  {prev_link}
  {next_link}
</div>

<!-- MAIN PRODUCT -->
<div class="product-layout">

  <!-- GALLERY -->
  <div class="gallery">
    <div class="main-img-wrap">
      <img id="main-img" src="{imgs[0]}" alt="{p['name']}">
      {badge_label(p.get('badge',''))}
    </div>
    <div class="thumbs">{thumb_html}</div>
  </div>

  <!-- INFO -->
  <div class="info-panel">
    <p class="prod-cat">{section_label} · {p['category']}</p>
    <h1 class="prod-name">{p['name']}</h1>
    <p class="prod-price">{p['price']}</p>
    <p class="making-note">Making Charges: {p['making']} &nbsp;|&nbsp; Price may vary with live rates</p>
    <div class="divider"></div>

    <div class="specs-table">{specs_html}</div>

    <p class="prod-desc">{p['desc']}</p>

    <p class="features-title">Product Highlights</p>
    <ul class="features-list">{features_html}</ul>

    <div class="cta-buttons">
      <a href="https://wa.me/{PHONE}?text={wa_encoded}" target="_blank" class="btn-wa-big">
        <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
        Enquire on WhatsApp
      </a>
      <a href="../index.html#{section_id}" class="btn-back">← Back to {section_label}</a>
    </div>

    <div class="trust-row">
      <div class="trust-item"><span class="trust-icon">🏅</span> BIS Hallmarked</div>
      <div class="trust-item"><span class="trust-icon">🔄</span> Lifetime Buyback</div>
      <div class="trust-item"><span class="trust-icon">✨</span> Free Polishing</div>
      <div class="trust-item"><span class="trust-icon">📦</span> Gift Packaging</div>
    </div>
  </div>
</div>

<!-- RELATED -->
{f"""<div class="related-section">
  <h2 class="related-title">You May Also Like</h2>
  <p class="related-sub">More {p['category']} from our collection</p>
  <div class="related-grid">{related_html}</div>
</div>""" if related_html else ''}

<footer>
  © 2025 <span>Nandgaonkar Jewellers</span> · Nashik, Maharashtra · <a href="https://wa.me/{PHONE}" style="color:{accent}">+91 95183 56108</a>
</footer>

<script>
function setMain(el, src) {{
  document.getElementById('main-img').src = src;
  document.querySelectorAll('.thumb').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
}}
</script>
</body>
</html>'''
    return html

# Generate gold pages
for i, p in enumerate(gold_products):
    imgs = GOLD_IMG_SETS[i % len(GOLD_IMG_SETS)]
    prev_id = gold_products[i-1]['id'] if i > 0 else None
    next_id = gold_products[i+1]['id'] if i < len(gold_products)-1 else None
    html = make_page(p, 'gold', imgs, prev_id, next_id, gold_products)
    with open(f'{OUT}/{p["id"]}.html', 'w', encoding='utf-8') as f:
        f.write(html)

# Generate silver pages
for i, p in enumerate(silver_products):
    imgs = SILVER_IMG_SETS[i % len(SILVER_IMG_SETS)]
    prev_id = silver_products[i-1]['id'] if i > 0 else None
    next_id = silver_products[i+1]['id'] if i < len(silver_products)-1 else None
    html = make_page(p, 'silver', imgs, prev_id, next_id, silver_products)
    with open(f'{OUT}/{p["id"]}.html', 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Generated {len(gold_products) + len(silver_products)} product pages!")

def generate_homepage():
    all_cards = ""

    for p in gold_products:
        img = GOLD_IMG_SETS[gold_products.index(p) % len(GOLD_IMG_SETS)][0]

        all_cards += f"""
        <div class="product-card">
            <a href="products/{p['id']}.html">
                <img src="{img}" alt="{p['name']}">
            </a>

            <div class="card-body">
                <p class="card-category">{p['category']}</p>
                <h3>{p['name']}</h3>
                <p class="price">{p['price']}</p>

                <a class="btn" href="products/{p['id']}.html">
                    View Product
                </a>
            </div>
        </div>
        """

    for p in silver_products:
        img = SILVER_IMG_SETS[silver_products.index(p) % len(SILVER_IMG_SETS)][0]

        all_cards += f"""
        <div class="product-card">
            <a href="products/{p['id']}.html">
                <img src="{img}" alt="{p['name']}">
            </a>

            <div class="card-body">
                <p class="card-category">{p['category']}</p>
                <h3>{p['name']}</h3>
                <p class="price">{p['price']}</p>

                <a class="btn" href="products/{p['id']}.html">
                    View Product
                </a>
            </div>
        </div>
        """

    homepage = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Nandgaonkar Jewellers</title>

<style>

body {{
    font-family: Arial;
    background:#faf6ef;
    margin:0;
}}

.header {{
    background:black;
    color:white;
    padding:40px;
    text-align:center;
}}

.grid {{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:20px;
    padding:40px;
}}

.product-card {{
    background:white;
    border:1px solid #ddd;
    overflow:hidden;
}}

.product-card img {{
    width:100%;
    height:260px;
    object-fit:cover;
}}

.card-body {{
    padding:15px;
}}

.price {{
    color:#8B6914;
    font-weight:bold;
}}

.btn {{
    display:inline-block;
    margin-top:10px;
    padding:10px 20px;
    background:#C9A84C;
    color:white;
    text-decoration:none;
}}

</style>
</head>

<body>

<div class="header">
    <h1>Nandgaonkar Jewellers</h1>
    <p>Gold & Silver Collection</p>
</div>

<div class="grid">
    {all_cards}
</div>

</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(homepage)



# ==========================================
# WEBSITE HOMEPAGE GENERATOR
# ==========================================

def product_card(p, img, is_gold=True):

    badge = badge_label(p.get('badge', ''))

    section = "gold" if is_gold else "silver"

    return f"""
    <div class="card">

        <div class="card-img-wrap">

            {badge}

            <img src="{img}" alt="{p['name']}">

        </div>

        <div class="card-body">

            <p class="card-category">
                {p['category']}
            </p>

            <h3 class="card-name">
                {p['name']}
            </h3>

            <p class="card-price">
                {p['price']}
            </p>

            <a href="products/{p['id']}.html"
               class="card-btn">

               View Details

            </a>

        </div>

    </div>
    """


def generate_homepage():

    gold_cards = ""
    silver_cards = ""

    # GOLD
    for i, p in enumerate(gold_products):

        img = GOLD_IMG_SETS[i % len(GOLD_IMG_SETS)][0]

        gold_cards += product_card(
            p,
            img,
            True
        )

    # SILVER
    for i, p in enumerate(silver_products):

        img = SILVER_IMG_SETS[i % len(SILVER_IMG_SETS)][0]

        silver_cards += product_card(
            p,
            img,
            False
        )

    homepage = f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>
Nandgaonkar Jewellers
</title>

<link rel="preconnect"
      href="https://fonts.googleapis.com">

<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=Cinzel:wght@400;600;700&family=Jost:wght@300;400;500&display=swap"
      rel="stylesheet">

<style>

:root {{

  --gold:#C9A84C;
  --gold-light:#E8D48B;
  --gold-dark:#8B6914;

  --silver:#7B8B9B;

  --bg:#0D0D0D;
  --cream:#FAF6EF;
  --text:#2C2C2C;

}}

* {{
  margin:0;
  padding:0;
  box-sizing:border-box;
}}

body {{
  background:var(--cream);
  color:var(--text);
  font-family:'Jost',sans-serif;
}}

.hero {{

  min-height:100vh;

  background:
  radial-gradient(circle at center,
  rgba(201,168,76,0.18),
  transparent 50%),
  #050505;

  display:flex;
  flex-direction:column;
  justify-content:center;
  align-items:center;

  text-align:center;

  padding:40px;

}}

.hero-top {{
  color:var(--gold);
  letter-spacing:6px;
  font-size:12px;
  margin-bottom:20px;
}}

.hero h1 {{

  font-family:'Cinzel',serif;
  font-size:clamp(3rem,9vw,7rem);
  line-height:0.95;

  color:white;

}}

.hero h1 span {{
  color:var(--gold-light);
}}

.hero-sub {{

  margin-top:30px;

  font-family:'Cormorant Garamond',serif;

  font-size:2rem;

  color:#C7B299;

}}

.hero-btns {{

  display:flex;
  gap:20px;

  margin-top:50px;
  flex-wrap:wrap;

}}

.hero-btn {{

  padding:18px 34px;

  text-decoration:none;

  border:1px solid var(--gold);

  color:white;

  letter-spacing:3px;

  font-size:13px;

  transition:0.3s;

}}

.hero-btn.gold {{
  background:linear-gradient(
  135deg,
  var(--gold),
  var(--gold-light)
  );

  color:black;
}}

.hero-btn:hover {{
  transform:translateY(-3px);
}}

.section {{

  padding:100px 40px;

}}

.section-title {{

  text-align:center;

  font-family:'Cinzel',serif;

  font-size:3rem;

  margin-bottom:15px;

}}

.section-sub {{

  text-align:center;

  color:#777;

  margin-bottom:60px;

  font-family:'Cormorant Garamond',serif;

  font-size:1.4rem;

}}

.grid {{

  display:grid;

  grid-template-columns:
  repeat(auto-fit,minmax(260px,1fr));

  gap:30px;

}}

.card {{

  background:white;

  border:1px solid #eee;

  overflow:hidden;

  transition:0.3s;

}}

.card:hover {{

  transform:translateY(-6px);

  box-shadow:
  0 16px 40px rgba(0,0,0,0.08);

}}

.card-img-wrap {{

  position:relative;

  aspect-ratio:1/1;

  overflow:hidden;

}}

.card img {{

  width:100%;
  height:100%;

  object-fit:cover;

}}

.card-body {{
  padding:20px;
}}

.card-category {{

  font-size:11px;

  letter-spacing:2px;

  color:var(--gold);

  margin-bottom:10px;

}}

.card-name {{

  font-family:'Cinzel',serif;

  font-size:20px;

  margin-bottom:12px;

}}

.card-price {{

  font-family:'Cinzel',serif;

  color:var(--gold-dark);

  font-size:1.3rem;

  margin-bottom:16px;

}}

.card-btn {{

  display:inline-block;

  text-decoration:none;

  padding:12px 20px;

  background:black;

  color:white;

  font-size:12px;

  letter-spacing:2px;

}}

footer {{

  background:black;

  color:rgba(255,255,255,0.5);

  text-align:center;

  padding:40px;

}}

.badge {{

  position:absolute;

  top:15px;
  left:15px;

  z-index:5;

  padding:6px 12px;

  font-size:11px;

  color:white;

}}

.badge-best {{
  background:#C9A84C;
}}

.badge-new {{
  background:#2C6B2F;
}}

.badge-hot {{
  background:#B22222;
}}

</style>
</head>

<body>

<section class="hero">

  <div class="hero-top">
    EST. SINCE 1970 · KARANJA LAD
  </div>

  <h1>
    NANDGAONKAR
    <br>
    <span>JEWELLERS</span>
  </h1>

  <p class="hero-sub">
    Crafting Timeless Beauty in Gold & Silver
  </p>

  <div class="hero-btns">

    <a href="#gold"
       class="hero-btn gold">

       ✦ GOLD COLLECTION

    </a>

    <a href="#silver"
       class="hero-btn">

       ◈ SILVER COLLECTION

    </a>

  </div>

</section>

<section class="section" id="gold">

  <h2 class="section-title">
    Gold Collection
  </h2>

  <p class="section-sub">
    Bridal • Temple • Daily Wear
  </p>

  <div class="grid">

    {gold_cards}

  </div>

</section>

<section class="section" id="silver">

  <h2 class="section-title">
    Silver Collection
  </h2>

  <p class="section-sub">
    Sterling • Oxidised • Devotional
  </p>

  <div class="grid">

    {silver_cards}

  </div>

</section>

<footer>

  © 2026 Nandgaonkar Jewellers · Karanja Lad

</footer>

</body>
</html>
"""

    with open(
        "index.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(homepage)

    print("Generated index.html")

generate_homepage()
