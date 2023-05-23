import pandas as pd

def phone(dtf,phone,clean=None):

                ### All Phones ###
    all_phones = dtf.drop_duplicates(subset='Title',keep='last')
    if clean == 'yes':
        all_phones_fake = all_phones.where(all_phones.Title.str.contains('fake|Fake|FAKE|faux|Faux|FAUX|clone|Clone|CLONE|replica|Replica|REPLICA|copy|Copy|recher|cherche|Cherche|looking|Recher|recher|Looking|change|CHANGE|trade|TRADE|&|et|haque|HAQUE|each|Each|EACH|with|With|WITH|case|Case|CASE|étui|ÉTUI|débloquer+|locked|icloud|Icloud|ICLOUD|cracked|Cracked|CRACKED|endommagé|broken|craque|Craque|CRAQUE|cracké|cracker|Cracké|CRACKÉ|CRACKER|cover|Cover|COVER|crack|Crack|CRACK')).dropna()
    else:
        all_phones_fake = all_phones.where(all_phones.Title.str.contains('fake|Fake|FAKE|faux|Faux|FAUX|clone|Clone|CLONE|replica|Replica|REPLICA|copy|Copy|change|CHANGE|trade|TRADE|locked|icloud|Icloud|ICLOUD')).dropna()
    all_phones = all_phones.drop(all_phones_fake.index).dropna()
    all_phones.reset_index(drop=True,inplace=True)

                ### IPHONE ###
    ### IPHONE 6 ###
    iphone_6 = all_phones.where(all_phones.Title.str.contains('phone 6|Phone 6|PHONE 6|phone6|Phone6|PHONE6')).dropna()


    # Cleaning false positives in iphone_6
    other_5 = iphone_6.where(iphone_6.Title.str.contains('phone 5|Phone 5|PHONE 5|phone5|Phone5|PHONE5')).dropna()
    other_7 = iphone_6.where(iphone_6.Title.str.contains('phone 7|Phone 7|PHONE 7|phone7|Phone7|PHONE7')).dropna()
    other_8 = iphone_6.where(iphone_6.Title.str.contains('phone 8|Phone 8|PHONE 8|phone8|Phone8|PHONE8')).dropna()
    other_X = iphone_6.where(iphone_6.Title.str.contains('phone x|Phone x|PHONE x|phone X|Phone X|PHONE X|phonex|Phonex|PHONEx|phoneX|PhoneX|PHONEX')).dropna()
    other = iphone_6.where(iphone_6.Title.str.contains('samsung|Samsung|SAMSUNG|s5|s6|s7|s8|s9|S5|S6|S7|S8|S9|Lg|LG')).dropna()
    all_other = other_5.append(other_7).append(other_8).append(other_X).append(other).dropna()

    # iphone_6 cleaned
    iphone_6.drop(all_other.index,inplace=True)

    # iphone_6 models
    iphone_6s = iphone_6.where(iphone_6.Title.str.contains('6s|6S|6 s|6 S|s6|S6|s 6|S 6')).dropna()

    iphone_6_plus = iphone_6.where(iphone_6.Title.str.contains('plus|Plus|PLUS|pLUS|6\+')).dropna()

    iphone_6s_plus = iphone_6.where(iphone_6.Title.str.contains('6s plus|6S Plus|6s PLUS|6S plus|6S PLUS|6 splus|6 SPlus|6 sPLUS|6 Splus|6 SPLUS|6 s plus|6 S Plus|6 s PLUS|6 S plus|6 S PLUS|6splus|6SPlus|6sPLUS|6Splus|6SPLUS|6 plus s|6 plus S|6 Plus s|6 Plus S|6 PLUS s|6 PLUS S|6plusS|6PlusS|6PLUSs|6s\+|6S\+')).dropna()


    all_iphone6_models = iphone_6s.append(iphone_6_plus).append(iphone_6s_plus).dropna()

    # 6s and 6 plus false positives
    iphone_6s_falsep = iphone_6s.where(iphone_6s.Title.str.contains('plus|Plus|PLUS|6\+|6s\+|6S\+')).dropna()
    iphone_6_plus_falsep = iphone_6_plus.where(iphone_6_plus.Title.str.contains('6s|6S|6 s|6 S|s plus|S plus|s Plus|S Plus|s PLUS|S PLUS|splus|Splus|sPlus|SPlus|sPLUS|SPLUS|plus s|plus S|Plus s|Plus S|PLUS s|PLUS S|plusS|PlusS|s\+|S\+')).dropna()

    # iphone_6 cleaned from models
    iphone_6.drop(all_iphone6_models.index,inplace=True)
    iphone_6s.drop(iphone_6s_falsep.index,inplace=True)
    iphone_6_plus.drop(iphone_6_plus_falsep.index,inplace=True)

    # Iphone 6 Gigs

    iphone_6_16g = iphone_6.where(iphone_6.Title.str.contains('16|16g|16G')).dropna()
    iphone_6_32g = iphone_6.where(iphone_6.Title.str.contains('32|32g|32G')).dropna()
    iphone_6_64g = iphone_6.where(iphone_6.Title.str.contains('64|64g|64G')).dropna()
    iphone_6_128g = iphone_6.where(iphone_6.Title.str.contains('128|128g|128G')).dropna()

    iphone_6s_16g = iphone_6s.where(iphone_6s.Title.str.contains('16|16g|16G')).dropna()
    iphone_6s_32g = iphone_6s.where(iphone_6s.Title.str.contains('32|32g|32G')).dropna()
    iphone_6s_64g = iphone_6s.where(iphone_6s.Title.str.contains('64|64g|64G')).dropna()
    iphone_6s_128g = iphone_6s.where(iphone_6s.Title.str.contains('128|128g|128G')).dropna()

    iphone_6_plus_16g = iphone_6_plus.where(iphone_6_plus.Title.str.contains('16|16g|16G')).dropna()
    iphone_6_plus_64g = iphone_6_plus.where(iphone_6_plus.Title.str.contains('64|64g|64G')).dropna()
    iphone_6_plus_128g = iphone_6_plus.where(iphone_6_plus.Title.str.contains('128|128g|128G')).dropna()

    iphone_6s_plus_16g = iphone_6s_plus.where(iphone_6s_plus.Title.str.contains('16|16g|16G')).dropna()
    iphone_6s_plus_32g = iphone_6s_plus.where(iphone_6s_plus.Title.str.contains('32|32g|32G')).dropna()
    iphone_6s_plus_64g = iphone_6s_plus.where(iphone_6s_plus.Title.str.contains('64|64g|64G')).dropna()
    iphone_6s_plus_128g = iphone_6s_plus.where(iphone_6s_plus.Title.str.contains('128|128g|128G')).dropna()


    ### IPHONE 7 ###
    iphone_7 = all_phones.where(all_phones.Title.str.contains('phone 7|Phone 7|PHONE 7|phone7|Phone7|PHONE7')).dropna()

    # Cleaning false positives in iphone_7
    other_5 = iphone_7.where(iphone_7.Title.str.contains('phone 5|Phone 5|PHONE 5|phone5|Phone5|PHONE5')).dropna()
    other_6 = iphone_7.where(iphone_7.Title.str.contains('phone 6|Phone 6|PHONE 6|phone6|Phone6|PHONE6')).dropna()
    other_8 = iphone_7.where(iphone_7.Title.str.contains('phone 8|Phone 8|PHONE 8|phone8|Phone8|PHONE8')).dropna()
    other_X = iphone_7.where(iphone_7.Title.str.contains('phone x|Phone x|PHONE x|phone X|Phone X|PHONE X|phonex|Phonex|PHONEx|phoneX|PhoneX|PHONEX')).dropna()
    other = iphone_7.where(iphone_7.Title.str.contains('samsung|Samsung|SAMSUNG|s5|s6|s7|s8|s9|S5|S6|S7|S8|S9|Lg|LG')).dropna()
    all_other = other_5.append(other_6).append(other_8).append(other_X).append(other).dropna()

    # iphone_7 cleaned
    iphone_7.drop(all_other.index,inplace=True)

    # iphone_7 models
    iphone_7_plus = iphone_7.where(iphone_7.Title.str.contains('plus|Plus|PLUS|pLUS|7\+')).dropna()

    # iphone_7 cleaned from models
    iphone_7.drop(iphone_7_plus.index,inplace=True)

    # Iphone 7 Gigs

    iphone_7_32g = iphone_7.where(iphone_7.Title.str.contains('32|32g|32G')).dropna()
    iphone_7_128g = iphone_7.where(iphone_7.Title.str.contains('128|128g|128G')).dropna()
    iphone_7_256g = iphone_7.where(iphone_7.Title.str.contains('256|256g|256G')).dropna()

    iphone_7_plus_32g = iphone_7_plus.where(iphone_7_plus.Title.str.contains('32|32g|32G')).dropna()
    iphone_7_plus_128g = iphone_7_plus.where(iphone_7_plus.Title.str.contains('128|128g|128G')).dropna()
    iphone_7_plus_256g = iphone_7_plus.where(iphone_7_plus.Title.str.contains('256|256g|256G')).dropna()



     ### IPHONE 8 ###
    iphone_8 = all_phones.where(all_phones.Title.str.contains('phone 8|Phone 8|PHONE 8|phone 8|Phone 8|PHONE 8|phone8|Phone8|PHONE8|phone8|Phone8|PHONE8')).dropna()

    # Cleaning false positives in iphone_8
    other_5 = iphone_8.where(iphone_8.Title.str.contains('phone 5|Phone 5|PHONE 5|phone5|Phone5|PHONE5')).dropna()
    other_6 = iphone_8.where(iphone_8.Title.str.contains('phone 6|Phone 6|PHONE 6|phone6|Phone6|PHONE6')).dropna()
    other_7 = iphone_8.where(iphone_8.Title.str.contains('phone 7|Phone 7|PHONE 7|phone7|Phone7|PHONE7')).dropna()
    other_X = iphone_8.where(iphone_8.Title.str.contains('phone x|Phone x|PHONE x|phone X|Phone X|PHONE X|phonex|Phonex|PHONEx|phoneX|PhoneX|PHONEX')).dropna()
    other = iphone_8.where(iphone_8.Title.str.contains('samsung|Samsung|SAMSUNG|s5|s6|s7|s8|s9|S5|S6|S7|S8|S9|Lg|LG')).dropna()
    all_other = other_5.append(other_6).append(other_7).append(other_X).append(other).dropna()

    # iphone_8 cleaned
    iphone_8.drop(all_other.index,inplace=True)

    # iphone_8 models
    iphone_8_plus = iphone_8.where(iphone_8.Title.str.contains('plus|Plus|PLUS|pLUS|8\+')).dropna()

    # iphone_8 cleaned from models
    iphone_8.drop(iphone_8_plus.index,inplace=True)

    # Iphone 8 Gigs

    iphone_8_64g = iphone_8.where(iphone_8.Title.str.contains('64|64g|64G')).dropna()
    iphone_8_256g = iphone_8.where(iphone_8.Title.str.contains('256|256g|256G')).dropna()

    iphone_8_plus_64g = iphone_8_plus.where(iphone_8_plus.Title.str.contains('64|64g|64G')).dropna()
    iphone_8_plus_256g = iphone_8_plus.where(iphone_8_plus.Title.str.contains('256|256g|256G')).dropna()



    # ### IPHONE X ###
    iphone_x = all_phones.where(all_phones.Title.str.contains('phone x|Phone x|PHONE x|phone X|Phone X|PHONE X|phonex|Phonex|PHONEx|phoneX|PhoneX|PHONEX')).dropna()
    iphonex64 = iphone_x.where(iphone_x.Title.str.contains('64')).dropna()
    iphonex256 = iphone_x.where(iphone_x.Title.str.contains('256')).dropna()

                ### SAMSUNG ###
    # ### S6 ###
    s6 = all_phones.where(all_phones.Title.str.contains('s6|S6')).dropna()

    # Cleaning false positives in s6
    other = s6.where(s6.Title.str.contains('s5|s7|s8|s9|S5|S7|S8|S9|Lg|LG|phone|Phone|PHONE')).dropna()

    # S6 cleaned
    s6.drop(other.index,inplace=True)

    # S6 mdoels
    s6_edge = s6.where(s6.Title.str.contains('edge|Edge|EDGE')).dropna()

    # s6 cleaned from models
    s6.drop(s6_edge.index,inplace=True)

    # ### S7 ###
    s7 = all_phones.where(all_phones.Title.str.contains('s7|S7')).dropna()

    # Cleaning false positives in s7
    other = s7.where(s7.Title.str.contains('s5|s6|s8|s9|S5|S6|S8|S9|Lg|LG|phone|Phone|PHONE')).dropna()

    # S7 cleaned
    s7.drop(other.index,inplace=True)

    # S7 mdoels
    s7_edge = s7.where(s7.Title.str.contains('edge|Edge|EDGE')).dropna()

    # s7 cleaned from models
    s7.drop(s7_edge.index,inplace=True)

    # ### S8 ###
    s8 = all_phones.where(all_phones.Title.str.contains('s8|S8')).dropna()

    # Cleaning false positives in s8
    other = s8.where(s8.Title.str.contains('s5|s6|s7|s9|S5|S6|S7|S9|Lg|LG|phone|Phone|PHONE')).dropna()

    # S8 cleaned
    s8.drop(other.index,inplace=True)

    # S8 mdoels
    s8_plus = s8.where(s8.Title.str.contains('plus|Plus|PLUS|8\+|8 \+')).dropna()

    # s8 cleaned from models
    s8.drop(s8_plus.index,inplace=True)

    # ### S9 ###
    s9 = all_phones.where(all_phones.Title.str.contains('s9|S9')).dropna()

    # Cleaning false positives in s9
    other = s9.where(s9.Title.str.contains('s5|s6|s7|s8|S5|S6|S7|S8|Lg|LG|phone|Phone|PHONE')).dropna()

    # S9 cleaned
    s9.drop(other.index,inplace=True)

    # S9 mdoels
    s9_plus = s9.where(s9.Title.str.contains('plus|Plus|PLUS|9\+|9 \+')).dropna()

    # s9 cleaned from models
    s9.drop(s9_plus.index,inplace=True)




    if phone == 'iphone6':
        return iphone_6
    if phone == 'iphone6_16g':
        return iphone_6_16g
    if phone == 'iphone6_32g':
        return iphone_6_32g
    if phone == 'iphone6_64g':
        return iphone_6_64g
    if phone == 'iphone6_128g':
        return iphone_6_128g


    if phone == 'iphone6s':
        return iphone_6s
    if phone == 'iphone6s_16g':
        return iphone_6s_16g
    if phone == 'iphone6s_32g':
        return iphone_6s_32g
    if phone == 'iphone6s_64g':
        return iphone_6s_64g
    if phone == 'iphone6s_128g':
        return iphone_6s_128g






    if phone == 'iphone6plus':
        return iphone_6_plus
    if phone == 'iphone6_plus_16g':
        return iphone_6_plus_16g
    if phone == 'iphone6_plus_64g':
        return iphone_6_plus_64g
    if phone == 'iphone6_plus_128g':
        return iphone_6_plus_128g






    if phone =='iphone6splus':
        return iphone_6s_plus
    if phone == 'iphone6s_plus_16g':
        return iphone_6s_plus_16g
    if phone == 'iphone6s_plus_32g':
        return iphone_6s_plus_32g
    if phone == 'iphone6s_plus_64g':
        return iphone_6s_plus_64g
    if phone == 'iphone6s_plus_128g':
        return iphone_6s_plus_128g




    if phone == 'iphone7':
        return iphone_7
    if phone == 'iphone7_32g':
        return iphone_7_32g
    if phone == 'iphone7_128g':
        return iphone_7_128g
    if phone == 'iphone7_256g':
        return iphone_7_256g




    if phone == 'iphone7plus':
        return iphone_7_plus
    if phone == 'iphone7_plus_32g':
        return iphone_7_plus_32g
    if phone == 'iphone7_plus_128g':
        return iphone_7_plus_128g
    if phone == 'iphone7_plus_256g':
        return iphone_7_plus_256g


    if phone =='iphone8':
        return iphone_8
    if phone == 'iphone8_64g':
        return iphone_8_64g
    if phone == 'iphone8_256g':
        return iphone_8_256g


    if phone == 'iphone8plus':
        return iphone_8_plus
    if phone == 'iphone8_plus_64g':
        return iphone_8_plus_64g
    if phone == 'iphone8_plus_256g':
        return iphone_8_plus_256g

    if phone == 'iphonex':
        return iphone_x
    if phone == 'iphonex64':
        return iphonex64
    if phone == 'iphonex256':
        return iphonex256

    if phone == 's6':
        return s6
    if phone == 's6edge':
        return s6_edge
    if phone == 's7':
        return s7
    if phone == 's7edge':
        return s7_edge
    if phone == 's8':
        return s8
    if phone == 's8plus':
        return s8_plus
    if phone == 's9':
        return s9
    if phone == 's9plus':
        return s9_plus


    if phone == 'all':
        return all_phones
