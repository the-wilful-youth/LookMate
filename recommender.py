def recommend_styles(face_shape, gender="male"):
    recommendations = {
        "male": {
            "Oval": {
                "hairstyles": ["men/hairstyles/undercut.png", "men/hairstyles/slick_back.png"],
                "beards": ["men/beards/stubble.png", "men/beards/full_beard.png"]
            },
            "Round": {
                "hairstyles": ["men/hairstyles/pompadour.png", "men/hairstyles/faux_hawk.png"],
                "beards": ["men/beards/goatee.png", "men/beards/short_boxed.png"]
            },
            "Square": {
                "hairstyles": ["men/hairstyles/side_part.png", "men/hairstyles/buzz_cut.png"],
                "beards": ["men/beards/extended_goatee.png", "men/beards/balbo.png"]
            },
            "Heart": {
                "hairstyles": ["men/hairstyles/messy.png", "men/hairstyles/quiff.png"],
                "beards": ["men/beards/van_dyke.png", "men/beards/light_stubble.png"]
            },
        },
        "female": {
            "Oval": ["women/hairstyles/layered.png", "women/hairstyles/wavy.png"],
            "Round": ["women/hairstyles/long_straight.png", "women/hairstyles/high_ponytail.png"],
            "Square": ["women/hairstyles/side_bangs.png", "women/hairstyles/bob.png"],
            "Heart": ["women/hairstyles/curls.png", "women/hairstyles/pixie_cut.png"]
        }
    }

    return recommendations[gender].get(face_shape, [])
