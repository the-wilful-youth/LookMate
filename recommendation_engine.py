"""
Recommendation Engine for LookMate
Provides personalized hairstyle and beard recommendations based on face shape
Includes detailed explanations and styling instructions
"""

def get_detailed_recommendations(face_shape, gender):
    """
    Get detailed recommendations with explanations and styling tips
    
    Args:
        face_shape: Detected face shape (Oval, Round, Square, Heart, Oblong)
        gender: User's gender (Male, Female)
    
    Returns:
        dict: Contains detailed hairstyles, beards, explanations, and styling tips
    """
    
    detailed_recommendations = {
        "Male": {
            "Oval": {
                "best_hairstyles": [
                    {
                        "name": "Classic Pompadour",
                        "description": "Volume on top with shorter sides",
                        "why": "Your balanced proportions work with most styles - pompadour adds sophistication",
                        "styling": "Use pomade, blow-dry upward, maintain 2-4 inch height",
                        "celebrities": "Elvis Presley, David Beckham"
                    },
                    {
                        "name": "Textured Quiff",
                        "description": "Modern swept-back style with texture",
                        "why": "Adds dynamic volume while maintaining your natural balance",
                        "styling": "Apply styling cream, blow-dry forward then back, finish with light hold spray",
                        "celebrities": "Zayn Malik, Chris Hemsworth"
                    },
                    {
                        "name": "Side Part",
                        "description": "Classic professional look with defined part",
                        "why": "Timeless style that emphasizes your symmetrical features",
                        "styling": "Use comb to create sharp part, apply light pomade, comb to side",
                        "celebrities": "Ryan Gosling, Cary Grant"
                    }
                ],
                "best_beards": [
                    {
                        "name": "Full Beard",
                        "description": "Even coverage across face and neck",
                        "why": "Complements your balanced features without overpowering",
                        "styling": "Trim evenly to 1-2 inches, maintain clean neckline, use beard oil daily",
                        "celebrities": "Chris Evans, Jake Gyllenhaal"
                    },
                    {
                        "name": "Stubble (5 o'clock shadow)",
                        "description": "Short, maintained facial hair",
                        "why": "Adds subtle definition without hiding your natural face shape",
                        "styling": "Trim to 3-5mm every 2-3 days, keep edges clean",
                        "celebrities": "George Clooney, Bradley Cooper"
                    },
                    {
                        "name": "Circle Beard",
                        "description": "Goatee connected to mustache",
                        "why": "Modern and clean, creates focal point at center of face",
                        "styling": "Keep mustache and goatee 0.5-1 inch, shave cheeks clean",
                        "celebrities": "Robert Downey Jr., Johnny Depp"
                    }
                ]
            },
            "Round": {
                "best_hairstyles": [
                    {
                        "name": "High Fade with Volume on Top",
                        "description": "Short sides, voluminous top",
                        "why": "Creates vertical lines to elongate your face and add definition",
                        "styling": "Use volumizing mousse, blow-dry upward, keep sides tight (grade 1-2)",
                        "celebrities": "Kevin Hart, Jack Black"
                    },
                    {
                        "name": "Angular Fringe",
                        "description": "Diagonal bangs with height",
                        "why": "Angular lines add sharp definition to soft features",
                        "styling": "Cut fringe at angle, style forward and to side, use light wax",
                        "celebrities": "Ed Sheeran, Jonah Hill"
                    },
                    {
                        "name": "Undercut with Textured Top",
                        "description": "Disconnected sides with messy top",
                        "why": "Contrast between short and long creates length illusion",
                        "styling": "Fade sides to skin, keep top 3-4 inches, style with clay",
                        "celebrities": "Leonardo DiCaprio, Seth Rogen"
                    }
                ],
                "best_beards": [
                    {
                        "name": "Chinstrap Beard",
                        "description": "Beard line along jawline",
                        "why": "Creates angular jawline appearance, elongates face vertically",
                        "styling": "Trim along jaw edge, keep 3-5mm length, shave cheeks and neck",
                        "celebrities": "Lewis Hamilton, Usher"
                    },
                    {
                        "name": "Goatee (pointed)",
                        "description": "Chin-only beard extending downward",
                        "why": "Adds length to chin area, creates vertical emphasis",
                        "styling": "Grow 1-2 inches from chin, trim to point, shave rest of face",
                        "celebrities": "Howie Mandel, Guy Fieri"
                    },
                    {
                        "name": "Van Dyke",
                        "description": "Mustache and pointed goatee",
                        "why": "Creates angular appearance and draws eye vertically",
                        "styling": "Disconnect mustache from goatee, point goatee downward, trim regularly",
                        "celebrities": "Johnny Depp (Pirates era)"
                    }
                ]
            },
            "Square": {
                "best_hairstyles": [
                    {
                        "name": "Textured Crop",
                        "description": "Short all-over with choppy texture",
                        "why": "Softens your strong jawline with gentle, textured movement",
                        "styling": "Cut to 1-2 inches, use texturizing spray, style with fingers",
                        "celebrities": "Brad Pitt, Chris Hemsworth"
                    },
                    {
                        "name": "Messy Quiff",
                        "description": "Casual swept-up style",
                        "why": "Adds softness and movement to balance angular features",
                        "styling": "Apply sea salt spray, blow-dry loosely upward, tousle with hands",
                        "celebrities": "Henry Cavill, Tom Hardy"
                    },
                    {
                        "name": "Side Part with Volume",
                        "description": "Classic part with lifted roots",
                        "why": "Balances your strong features with elegant volume",
                        "styling": "Part deep on side, lift roots when drying, use medium hold pomade",
                        "celebrities": "Jon Hamm, Aaron Rodgers"
                    }
                ],
                "best_beards": [
                    {
                        "name": "Full Rounded Beard",
                        "description": "Full coverage with rounded shape",
                        "why": "Softens angular jaw with curved beard line",
                        "styling": "Grow 1-2 inches, trim in rounded shape, avoid sharp angles",
                        "celebrities": "Ben Affleck, Gerard Butler"
                    },
                    {
                        "name": "Circle Beard",
                        "description": "Rounded goatee with mustache",
                        "why": "Adds curves to balance geometric jawline",
                        "styling": "Keep circular shape, 0.5-1 inch length, blend edges softly",
                        "celebrities": "Robert Downey Jr."
                    },
                    {
                        "name": "Heavy Stubble",
                        "description": "Thick but short facial hair",
                        "why": "Maintains masculinity while avoiding harsh angular lines",
                        "styling": "Trim to 5-8mm, keep edges natural, use beard balm",
                        "celebrities": "Hugh Jackman, Jason Statham"
                    }
                ]
            },
            "Heart": {
                "best_hairstyles": [
                    {
                        "name": "Side Swept Fringe",
                        "description": "Bangs swept across forehead",
                        "why": "Balances wider forehead by adding coverage and side volume",
                        "styling": "Grow fringe to eyebrow, sweep to side, use light mousse",
                        "celebrities": "Justin Timberlake, Ryan Gosling"
                    },
                    {
                        "name": "Textured Crop with Side Volume",
                        "description": "Short with volume at temples",
                        "why": "Adds width at jawline to balance narrow chin",
                        "styling": "Keep sides slightly longer, texturize with clay, add volume at jaw level",
                        "celebrities": "Timothée Chalamet"
                    },
                    {
                        "name": "Medium Length with Layers",
                        "description": "Shoulder-length with movement",
                        "why": "Creates balance by distributing visual weight evenly",
                        "styling": "Layer from cheekbones down, use texturizing spray, style loosely",
                        "celebrities": "Jared Leto, Kit Harington"
                    }
                ],
                "best_beards": [
                    {
                        "name": "Full Beard (wider at bottom)",
                        "description": "Dense beard widening at chin",
                        "why": "Adds crucial width to narrow chin area, balances face proportions",
                        "styling": "Grow fuller at chin, trim sides shorter, create wider bottom",
                        "celebrities": "Chris Pine (with beard)"
                    },
                    {
                        "name": "Mutton Chops",
                        "description": "Sideburns extending to jaw",
                        "why": "Widens lower face appearance significantly",
                        "styling": "Grow thick sideburns to jaw angle, shave chin and mustache areas",
                        "celebrities": "Hugh Jackman (Wolverine)"
                    },
                    {
                        "name": "Extended Goatee",
                        "description": "Wide goatee with mustache",
                        "why": "Adds bulk to chin area without emphasizing forehead",
                        "styling": "Grow wide at chin, connect to mustache, keep 1-1.5 inches",
                        "celebrities": "Brad Pitt (various roles)"
                    }
                ]
            },
            "Oblong": {
                "best_hairstyles": [
                    {
                        "name": "Fringe/Bangs",
                        "description": "Horizontal bangs across forehead",
                        "why": "Shortens face visually by breaking up length",
                        "styling": "Cut to eyebrow level, style straight across, use light wax",
                        "celebrities": "Adam Levine, Keanu Reeves"
                    },
                    {
                        "name": "Side Part with Side Volume",
                        "description": "Deep part with fullness at sides",
                        "why": "Adds width to sides, balances elongated proportions",
                        "styling": "Part deep, add volume at ears, keep top flat",
                        "celebrities": "Benedict Cumberbatch, Nicolas Cage"
                    },
                    {
                        "name": "Wavy Medium Length",
                        "description": "Shoulder-length with waves",
                        "why": "Adds fullness to sides, creates horizontal emphasis",
                        "styling": "Grow to chin-length, enhance waves with sea salt spray",
                        "celebrities": "Jared Leto, Jason Momoa"
                    }
                ],
                "best_beards": [
                    {
                        "name": "Full Beard (rounded)",
                        "description": "Dense, horizontally-emphasized beard",
                        "why": "Adds width and shortens face appearance",
                        "styling": "Grow thick, trim in rounded shape, emphasize width over length",
                        "celebrities": "Joaquin Phoenix, Colin Farrell"
                    },
                    {
                        "name": "Mutton Chops (wide)",
                        "description": "Thick sideburns across face",
                        "why": "Widens appearance dramatically across mid-face",
                        "styling": "Grow sideburns thick and wide, connect if desired",
                        "celebrities": "Hugh Jackman"
                    },
                    {
                        "name": "Short Boxed Beard",
                        "description": "Square-shaped short beard",
                        "why": "Creates horizontal lines without adding face length",
                        "styling": "Keep 5-10mm, trim in boxy shape, clean lines",
                        "celebrities": "Idris Elba, Drake"
                    }
                ]
            }
        },
        "Female": {
            # Female recommendations remain the same but can be enhanced similarly
            "Oval": {
                "best_hairstyles": [
                    {
                        "name": "Long Layers",
                        "description": "Flowing layers throughout",
                        "why": "Enhances your natural balance with beautiful movement",
                        "styling": "Cut long layers from chin down, use volumizing spray at roots",
                        "celebrities": "Beyoncé, Jessica Alba"
                    },
                    {
                        "name": "Bob Cut",
                        "description": "Chin to shoulder length",
                        "why": "Classic and versatile, perfect for your proportions",
                        "styling": "Cut to chin or shoulder, style with round brush for volume",
                        "celebrities": "Taylor Swift, Emma Stone"
                    },
                    {
                        "name": "Pixie Cut",
                        "description": "Short and chic all-over",
                        "why": "Bold style that showcases your balanced features",
                        "styling": "Keep 1-3 inches, style with wax for texture",
                        "celebrities": "Halle Berry, Audrey Hepburn"
                    }
                ],
                "best_makeup": [
                    {
                        "name": "Natural Contour",
                        "tip": "Enhance your balanced features with subtle contouring",
                        "how": "Contour lightly under cheekbones, blend well for natural definition"
                    },
                    {
                        "name": "Balanced Eye and Lip",
                        "tip": "You can wear bold eyes OR bold lips equally well",
                        "how": "Experiment with both - smoky eyes with nude lips or red lips with minimal eyes"
                    }
                ]
            },
            "Round": {
                "best_hairstyles": [
                    {
                        "name": "Long Layers with Side Part",
                        "description": "Vertical layers past shoulders",
                        "why": "Creates length and frames face to elongate",
                        "styling": "Part deep to side, layer from chin down, style straight or wavy",
                        "celebrities": "Selena Gomez, Ginnifer Goodwin"
                    },
                    {
                        "name": "Angled Bob",
                        "description": "Longer in front, shorter in back",
                        "why": "Angular lines add definition and length",
                        "styling": "Cut longer at front (chin-length), short at nape, style sleek",
                        "celebrities": "Kelly Clarkson, Adele"
                    },
                    {
                        "name": "High Volume Updo",
                        "description": "Pulled up with height at crown",
                        "why": "Elongates face dramatically with vertical emphasis",
                        "styling": "Tease crown, pull hair up high, leave face-framing pieces",
                        "celebrities": "Mila Kunis, Emma Stone"
                    }
                ],
                "best_makeup": [
                    {
                        "name": "Contour Temples and Cheekbones",
                        "tip": "Add definition with strategic contouring",
                        "how": "Contour temples, under cheekbones, and along hairline to create angles"
                    },
                    {
                        "name": "Arched Eyebrows",
                        "tip": "Higher arch lifts and elongates face",
                        "how": "Shape brows with high, defined arch - avoid rounded brow shapes"
                    }
                ]
            },
            "Square": {
                "best_hairstyles": [
                    {
                        "name": "Soft Waves",
                        "description": "Loose, flowing waves",
                        "why": "Softens angular jawline with gentle curves",
                        "styling": "Use large barrel curling iron, create loose S-waves, finish with texturizing spray",
                        "celebrities": "Angelina Jolie, Olivia Wilde"
                    },
                    {
                        "name": "Layered Long Hair",
                        "description": "Layers from cheekbones down",
                        "why": "Adds movement and softness to balance strong features",
                        "styling": "Layer heavily from cheeks, add waves or keep straight with movement",
                        "celebrities": "Demi Moore, Sandra Bullock"
                    },
                    {
                        "name": "Side Swept Bangs",
                        "description": "Wispy fringe swept across",
                        "why": "Softens forehead and adds gentle framing",
                        "styling": "Cut long wispy bangs, sweep to side, keep feathered and soft",
                        "celebrities": "Keira Knightley"
                    }
                ],
                "best_makeup": [
                    {
                        "name": "Soft Rounded Contour",
                        "tip": "Soften jawline with rounded contouring technique",
                        "how": "Contour jaw corners in circular motion, blend upward toward ears"
                    },
                    {
                        "name": "Rounded Blush Placement",
                        "tip": "Apply blush in circular motions on apples of cheeks",
                        "how": "Smile and apply pink/peach blush on rounded part of cheeks"
                    }
                ]
            },
            "Heart": {
                "best_hairstyles": [
                    {
                        "name": "Chin-Length Bob",
                        "description": "Blunt cut at chin level",
                        "why": "Adds width at narrow chin to balance proportions",
                        "styling": "Cut straight across at chin, add slight curl outward at ends",
                        "celebrities": "Reese Witherspoon, Scarlett Johansson"
                    },
                    {
                        "name": "Side Swept Bangs",
                        "description": "Long fringe swept across forehead",
                        "why": "Minimizes wide forehead appearance",
                        "styling": "Cut long wispy bangs, sweep across forehead diagonally",
                        "celebrities": "Kerry Washington, Kourtney Kardashian"
                    },
                    {
                        "name": "Shoulder Length with Curls",
                        "description": "Medium length with volume at ends",
                        "why": "Adds width below cheekbones where needed",
                        "styling": "Cut to shoulders, curl bottom half outward for volume",
                        "celebrities": "Jennifer Love Hewitt"
                    }
                ],
                "best_makeup": [
                    {
                        "name": "Contour Temples",
                        "tip": "Narrow forehead appearance with temple contouring",
                        "how": "Apply darker contour at temples and hairline, blend toward center"
                    },
                    {
                        "name": "Highlight Chin and Jaw",
                        "tip": "Brighten lower face to add visual width",
                        "how": "Apply highlighter on chin point and along jawline"
                    }
                ]
            },
            "Oblong": {
                "best_hairstyles": [
                    {
                        "name": "Blunt Bangs",
                        "description": "Straight across forehead",
                        "why": "Shortens face length dramatically",
                        "styling": "Cut straight across at eyebrows, style flat and full",
                        "celebrities": "Liv Tyler, Sarah Jessica Parker"
                    },
                    {
                        "name": "Shoulder Length Waves",
                        "description": "Medium length with volume",
                        "why": "Adds width at sides to balance length",
                        "styling": "Cut to shoulders, add waves throughout for fullness",
                        "celebrities": "Alexa Chung"
                    },
                    {
                        "name": "Layered Bob with Volume",
                        "description": "Chin-length with fullness",
                        "why": "Creates horizontal emphasis and width",
                        "styling": "Cut layers at chin, tease for volume, avoid long straight styles",
                        "celebrities": "Sarah Jessica Parker"
                    }
                ],
                "best_makeup": [
                    {
                        "name": "Horizontal Contour",
                        "tip": "Contour along hairline and jawline horizontally",
                        "how": "Apply contour in horizontal lines at forehead and jaw to shorten appearance"
                    },
                    {
                        "name": "Fuller Eyebrows",
                        "tip": "Straight, fuller brows create horizontal lines",
                        "how": "Fill brows straight across, avoid high arches"
                    }
                ]
            }
        }
    }
    
    if gender in detailed_recommendations and face_shape in detailed_recommendations[gender]:
        return detailed_recommendations[gender][face_shape]
    
    return {
        "best_hairstyles": [],
        "best_beards": [] if gender == "Male" else [],
        "best_makeup": [] if gender == "Female" else []
    }


def get_recommendations(face_shape, gender):
    """
    Get personalized hairstyle and beard/makeup recommendations based on face shape and gender
    
    Args:
        face_shape: Detected face shape (Oval, Round, Square, Heart, Oblong)
        gender: User's gender (Male, Female)
    
    Returns:
        dict: Contains hairstyles, facial_styles, and styling_tips
    """
    
    recommendations = {
        "Male": {
            "Oval": {
                "hairstyles": [
                    "Classic Pompadour - Your balanced proportions work with most styles",
                    "Textured Quiff - Adds volume and modern appeal",
                    "Side Part - Timeless and professional",
                    "Slicked Back - Sleek and sophisticated",
                    "Messy Fringe - Casual and trendy"
                ],
                "beards": [
                    "Full Beard - Complements balanced features",
                    "Stubble - Adds subtle definition",
                    "Goatee - Creates focal point",
                    "Circle Beard - Modern and clean"
                ],
                "tips": [
                    "You have the most versatile face shape - experiment freely!",
                    "Most hairstyles and beard styles will suit you",
                    "Maintain symmetry for best results"
                ]
            },
            "Round": {
                "hairstyles": [
                    "High Fade with Volume on Top - Creates illusion of length",
                    "Angular Fringe - Adds definition",
                    "Undercut with Textured Top - Elongates face",
                    "Spiky Top - Adds height",
                    "Side Swept Style - Creates angles"
                ],
                "beards": [
                    "Chinstrap Beard - Elongates jawline",
                    "Goatee - Adds length to chin",
                    "Van Dyke - Creates angular appearance",
                    "Light Stubble with Defined Lines - Adds structure"
                ],
                "tips": [
                    "Add height on top to elongate your face",
                    "Keep sides shorter to create vertical lines",
                    "Beards with angular shapes work best",
                    "Avoid round, full beards that add width"
                ]
            },
            "Square": {
                "hairstyles": [
                    "Textured Crop - Softens strong jawline",
                    "Messy Quiff - Adds movement",
                    "Side Part with Volume - Balances angular features",
                    "Wavy Medium Length - Softens edges",
                    "Fringe Styles - Adds roundness"
                ],
                "beards": [
                    "Full Rounded Beard - Softens jaw angles",
                    "Circle Beard - Adds curves",
                    "Heavy Stubble - Maintains masculinity without harsh lines",
                    "Balbo - Adds dimension"
                ],
                "tips": [
                    "Soften your angular features with rounded styles",
                    "Add texture and movement to reduce sharpness",
                    "Rounded beards balance your strong jaw",
                    "Avoid styles that are too geometric"
                ]
            },
            "Heart": {
                "hairstyles": [
                    "Side Swept Fringe - Balances wider forehead",
                    "Textured Crop - Adds width at jawline",
                    "Medium Length with Layers - Creates balance",
                    "Quiff with Side Volume - Distributes visual weight",
                    "Faux Hawk - Draws attention centrally"
                ],
                "beards": [
                    "Full Beard - Adds width to narrow chin",
                    "Mutton Chops - Widens lower face",
                    "Chin Strap with Width - Balances proportions",
                    "Extended Goatee - Adds bulk to chin area"
                ],
                "tips": [
                    "Add volume at sides and chin to balance wider forehead",
                    "Avoid styles that add height at crown",
                    "Fuller beards help balance face proportions",
                    "Side-swept styles work particularly well"
                ]
            },
            "Oblong": {
                "hairstyles": [
                    "Fringe/Bangs - Shortens face visually",
                    "Side Part with Volume on Sides - Adds width",
                    "Textured Crop - Creates horizontal emphasis",
                    "Wavy Medium Length - Adds fullness to sides",
                    "Low Fade - Keeps proportions balanced"
                ],
                "beards": [
                    "Full Beard - Adds width and shortens face",
                    "Mutton Chops - Widens appearance",
                    "Rounded Beard - Creates horizontal lines",
                    "Avoid Long Goatees - They elongate further"
                ],
                "tips": [
                    "Add width to sides to balance length",
                    "Avoid styles that add height on top",
                    "Horizontal lines work better than vertical",
                    "Fuller beards help shorten facial appearance"
                ]
            }
        },
        "Female": {
            "Oval": {
                "hairstyles": [
                    "Long Layers - Enhances natural balance",
                    "Bob Cut - Classic and versatile",
                    "Pixie Cut - Bold and chic",
                    "Beach Waves - Soft and romantic",
                    "High Ponytail - Elegant and lifted"
                ],
                "makeup": [
                    "Natural Contour - Enhance your balanced features",
                    "Subtle Blush on Apples of Cheeks",
                    "Any eyebrow shape works well",
                    "Balanced eye and lip makeup"
                ],
                "tips": [
                    "Your face shape is ideal - most styles suit you!",
                    "Experiment with different lengths and textures",
                    "You can pull off both dramatic and subtle looks",
                    "Maintain natural symmetry"
                ]
            },
            "Round": {
                "hairstyles": [
                    "Long Layers with Side Part - Creates length",
                    "Angled Bob - Adds definition",
                    "High Volume Updo - Elongates face",
                    "Straight Hair with Center Part - Frames face",
                    "Layered Pixie - Adds height"
                ],
                "makeup": [
                    "Contour along cheekbones and temples",
                    "Highlight center of face vertically",
                    "Arched eyebrows to lift face",
                    "Avoid round blush application"
                ],
                "tips": [
                    "Add height and volume at crown",
                    "Keep hair away from cheeks",
                    "Long earrings elongate your face",
                    "Avoid blunt, horizontal bangs"
                ]
            },
            "Square": {
                "hairstyles": [
                    "Soft Waves - Softens angular jaw",
                    "Layered Long Hair - Adds movement",
                    "Side Swept Bangs - Softens forehead",
                    "Rounded Bob - Curves sharp edges",
                    "Wispy Pixie - Feminine and soft"
                ],
                "makeup": [
                    "Soft, rounded contour",
                    "Blush on apples of cheeks in circular motion",
                    "Soften jawline with bronzer",
                    "Rounded eyebrow shape"
                ],
                "tips": [
                    "Soften angles with curves and layers",
                    "Add movement and texture",
                    "Avoid severe, straight styles",
                    "Rounded shapes balance your features"
                ]
            },
            "Heart": {
                "hairstyles": [
                    "Chin-Length Bob - Balances narrow chin",
                    "Side Swept Bangs - Minimizes wide forehead",
                    "Shoulder Length with Curls - Adds width below",
                    "Low Bun - Creates balance",
                    "Wispy Fringe - Softens forehead"
                ],
                "makeup": [
                    "Contour temples to narrow forehead",
                    "Highlight chin and jawline",
                    "Add width with blush along cheekbones",
                    "Straight or slightly arched brows"
                ],
                "tips": [
                    "Add width at chin level",
                    "Minimize forehead width with side parts",
                    "Avoid top-heavy styles",
                    "Balance proportions with strategic volume"
                ]
            },
            "Oblong": {
                "hairstyles": [
                    "Blunt Bangs - Shortens face length",
                    "Shoulder Length Waves - Adds width",
                    "Layered Bob with Volume - Creates fullness",
                    "Side Part with Curls - Widens face",
                    "Avoid Very Long Straight Hair"
                ],
                "makeup": [
                    "Horizontal contour along hairline and jawline",
                    "Blush placed horizontally on cheeks",
                    "Straight, fuller eyebrows",
                    "Avoid vertical highlighting"
                ],
                "tips": [
                    "Add width with volume at sides",
                    "Bangs help shorten face appearance",
                    "Avoid center parts and high updos",
                    "Create horizontal emphasis"
                ]
            }
        }
    }
    
    # Get recommendations for the specific face shape and gender
    if gender in recommendations and face_shape in recommendations[gender]:
        return recommendations[gender][face_shape]
    
    # Default fallback
    return {
        "hairstyles": ["Consult with a professional stylist for personalized advice"],
        "facial_styles": ["Natural style suits all face shapes"],
        "tips": ["Every face shape is unique and beautiful!"]
    }


def format_recommendations_display(face_shape, gender):
    """
    Format recommendations for display in the UI
    
    Args:
        face_shape: Detected face shape
        gender: User's gender
    
    Returns:
        str: Formatted HTML string for display
    """
    recs = get_recommendations(face_shape, gender)
    
    facial_key = "beards" if gender == "Male" else "makeup"
    facial_label = "Beard Styles" if gender == "Male" else "Makeup Tips"
    
    html = f"""
    <div style="color: #ded1c6;">
        <h3 style="color: #ded1c6; margin-top: 1.5rem;">💇 Recommended Hairstyles</h3>
        <ul>
    """
    
    for style in recs.get("hairstyles", []):
        html += f"<li style='margin: 0.5rem 0; color: #ded1c6;'>{style}</li>"
    
    html += f"""
        </ul>
        <h3 style="color: #ded1c6; margin-top: 1.5rem;">✨ {facial_label}</h3>
        <ul>
    """
    
    facial_styles = recs.get(facial_key, recs.get("makeup", []))
    for style in facial_styles:
        html += f"<li style='margin: 0.5rem 0; color: #ded1c6;'>{style}</li>"
    
    html += f"""
        </ul>
        <h3 style="color: #ded1c6; margin-top: 1.5rem;">💡 Styling Tips</h3>
        <ul>
    """
    
    for tip in recs.get("tips", []):
        html += f"<li style='margin: 0.5rem 0; color: #ded1c6;'>{tip}</li>"
    
    html += """
        </ul>
    </div>
    """
    
    return html


def format_detailed_recommendations_display(face_shape, gender):
    """
    Format detailed recommendations with styling instructions and celebrity examples
    
    Args:
        face_shape: Detected face shape
        gender: User's gender
    
    Returns:
        str: Formatted HTML string for display
    """
    recs = get_detailed_recommendations(face_shape, gender)
    
    html = f"""
    <div style="color: #ded1c6;">
        <h2 style="color: #ded1c6; text-align: center; margin-bottom: 2rem; font-size: 2rem;">
            ✨ Personalized Style Guide for {face_shape} Face Shape ✨
        </h2>
    """
    
    # Hairstyles Section
    if "best_hairstyles" in recs and recs["best_hairstyles"]:
        html += """
        <div style="background: rgba(0, 0, 0, 0.3); padding: 1.5rem; border-radius: 10px; margin-bottom: 2rem;">
            <h3 style="color: #a77693; margin-bottom: 1.5rem; font-size: 1.5rem;">
                💇 Best Hairstyles for You
            </h3>
        """
        
        for i, style in enumerate(recs["best_hairstyles"], 1):
            html += f"""
            <div style="background: rgba(15, 45, 77, 0.5); padding: 1.2rem; margin-bottom: 1rem; border-radius: 8px; border-left: 4px solid #a77693;">
                <h4 style="color: #ded1c6; margin-bottom: 0.5rem; font-size: 1.2rem;">
                    {i}. {style['name']}
                </h4>
                <p style="color: #ded1c6; margin: 0.5rem 0; font-style: italic;">
                    <strong>Style:</strong> {style['description']}
                </p>
                <p style="color: #a77693; margin: 0.5rem 0;">
                    <strong>💡 Why it works:</strong> {style['why']}
                </p>
                <p style="color: #ded1c6; margin: 0.5rem 0;">
                    <strong>✂️ How to style:</strong> {style['styling']}
                </p>
                <p style="color: #e8d5c4; margin: 0.5rem 0; font-size: 0.9rem;">
                    <strong>🌟 Celebrity examples:</strong> {style['celebrities']}
                </p>
            </div>
            """
        html += "</div>"
    
    # Beards Section (Male)
    if gender == "Male" and "best_beards" in recs and recs["best_beards"]:
        html += """
        <div style="background: rgba(0, 0, 0, 0.3); padding: 1.5rem; border-radius: 10px; margin-bottom: 2rem;">
            <h3 style="color: #a77693; margin-bottom: 1.5rem; font-size: 1.5rem;">
                🧔 Best Beard Styles for You
            </h3>
        """
        
        for i, beard in enumerate(recs["best_beards"], 1):
            html += f"""
            <div style="background: rgba(15, 45, 77, 0.5); padding: 1.2rem; margin-bottom: 1rem; border-radius: 8px; border-left: 4px solid #a77693;">
                <h4 style="color: #ded1c6; margin-bottom: 0.5rem; font-size: 1.2rem;">
                    {i}. {beard['name']}
                </h4>
                <p style="color: #ded1c6; margin: 0.5rem 0; font-style: italic;">
                    <strong>Style:</strong> {beard['description']}
                </p>
                <p style="color: #a77693; margin: 0.5rem 0;">
                    <strong>💡 Why it works:</strong> {beard['why']}
                </p>
                <p style="color: #ded1c6; margin: 0.5rem 0;">
                    <strong>✂️ How to maintain:</strong> {beard['styling']}
                </p>
                <p style="color: #e8d5c4; margin: 0.5rem 0; font-size: 0.9rem;">
                    <strong>🌟 Celebrity examples:</strong> {beard['celebrities']}
                </p>
            </div>
            """
        html += "</div>"
    
    # Makeup Section (Female)
    if gender == "Female" and "best_makeup" in recs and recs["best_makeup"]:
        html += """
        <div style="background: rgba(0, 0, 0, 0.3); padding: 1.5rem; border-radius: 10px; margin-bottom: 2rem;">
            <h3 style="color: #a77693; margin-bottom: 1.5rem; font-size: 1.5rem;">
                💄 Makeup Tips for Your Face Shape
            </h3>
        """
        
        for i, makeup in enumerate(recs["best_makeup"], 1):
            html += f"""
            <div style="background: rgba(15, 45, 77, 0.5); padding: 1.2rem; margin-bottom: 1rem; border-radius: 8px; border-left: 4px solid #a77693;">
                <h4 style="color: #ded1c6; margin-bottom: 0.5rem; font-size: 1.2rem;">
                    {i}. {makeup['name']}
                </h4>
                <p style="color: #a77693; margin: 0.5rem 0;">
                    <strong>💡 Tip:</strong> {makeup['tip']}
                </p>
                <p style="color: #ded1c6; margin: 0.5rem 0;">
                    <strong>✨ How to apply:</strong> {makeup['how']}
                </p>
            </div>
            """
        html += "</div>"
    
    # General Tips
    html += """
        <div style="background: linear-gradient(135deg, #a77693, #ded1c6); padding: 1.5rem; border-radius: 10px; margin-top: 2rem;">
            <h3 style="color: #0f2d4d; margin-bottom: 1rem; font-size: 1.3rem;">
                💡 Pro Tips
            </h3>
            <ul style="color: #0f2d4d; margin: 0;">
                <li style="margin: 0.7rem 0;">Consult with a professional stylist for personalized adjustments</li>
                <li style="margin: 0.7rem 0;">Show them photos of celebrity examples to communicate your vision</li>
                <li style="margin: 0.7rem 0;">Consider your hair texture and lifestyle when choosing styles</li>
                <li style="margin: 0.7rem 0;">Don't be afraid to experiment - hair grows back!</li>
            </ul>
        </div>
    </div>
    """
    
    return html
