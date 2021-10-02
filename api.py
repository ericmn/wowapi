from .endpoint import endpoint
from .namespaces import static, dynamic, profile
from .schema import Realm, Item, CharacterPet, Pet


@endpoint(namespace=static)
def achievement_category_index():
    return f"/data/wow/achievement-category/index"


@endpoint(namespace=static)
def achievement_category(*, achievementCategoryId):
    return f"/data/wow/achievement-category/{achievementCategoryId}"


@endpoint(namespace=static)
def achievement_index():
    return f"/data/wow/achievement/index"


@endpoint(namespace=static)
def achievement(*, achievementId):
    return f"/data/wow/achievement/{achievementId}"


@endpoint(namespace=static)
def achievement_media(*, achievementId):
    return f"/data/wow/media/achievement/{achievementId}"


@endpoint(namespace=dynamic, index='auctions')
def auctions(*, connectedRealmId):
    return f"/data/wow/connected-realm/{connectedRealmId}/auctions"


@endpoint(namespace=dynamic, index='connected_realms')
def connected_realm_index():
    return f"/data/wow/connected-realm/index"


@endpoint(namespace=dynamic)
def connected_realm(*, connectedRealmId):
    return f"/data/wow/connected-realm/{connectedRealmId}"
# def connected_realm_search


@endpoint(namespace=static)
def creature_family_index():
    return f"/data/wow/creature-family/index"


@endpoint(namespace=static)
def creature_family(*, creatureFamilyId):
    return f"/data/wow/creature-family/{creatureFamilyId}"


@endpoint(namespace=static)
def creature_type(*, creatureTypeId):
    return f"/data/wow/creature-type/{creatureTypeId}"
# def creature_search


@endpoint(namespace=static)
def creature_display_media(*, creatureDisplayId):
    return f"/data/wow/media/creature-display/{creatureDisplayId}"


@endpoint(namespace=static)
def creature_family_media(*, creatureFamilyId):
    return f"/data/wow/media/creature-family/{creatureFamilyId}"


@endpoint(namespace=static, index='item_classes')
def item_class_index():
    return f"/data/wow/item-class/index"


@endpoint(namespace=static)
def item_class(*, itemClassId):
    return f"/data/wow/item-class/{itemClassId}"


@endpoint(namespace=static)
def item_set_index():
    return f"/data/wow/item-set/index"


@endpoint(namespace=static)
def item_set(*, itemSetId):
    return f"/data/wow/item-set/{itemSetId}"


@endpoint(namespace=static)
def item_subclass(*, itemClassId, itemSubclassId):
    return f"/data/wow/item-class/{itemClassId}/item-subclass/{itemSubclassId}"


@endpoint(namespace=static, schema=Item)
def item(*, itemId):
    return f"/data/wow/item/{itemId}"


@endpoint(namespace=static)
def item_media(*, itemId):
    return f"/data/wow/media/item/{itemId}"
# def item_search


@endpoint(namespace=static)
def mount_index():
    return f"/data/wow/mount/index"


@endpoint(namespace=static)
def mount(*, mountId):
    return f"/data/wow/mount/{mountId}"
# def mount_search


@endpoint(namespace=static, schema=Pet, index='pets')
def pet_index():
    return f"/data/wow/pet/index"


@endpoint(namespace=static, schema=Pet)
def pet(*, petId):
    return f"/data/wow/pet/{petId}"


@endpoint(namespace=static)
def pet_media(*, petId):
    return f"/data/wow/media/pet/{petId}"


@endpoint(namespace=static, index='abilities')
def pet_ability_index():
    return f"/data/wow/pet-ability/index"


@endpoint(namespace=static)
def pet_ability(*, petAbilityId):
    return f"/data/wow/pet-ability/{petAbilityId}"


@endpoint(namespace=static)
def pet_ability_media(*, petAbilityId):
    return f"/data/wow/media/pet-ability/{petAbilityId}"


@endpoint(namespace=dynamic, schema=Realm, index='realms')
def realm_index():
    return f"/data/wow/realm/index"


@endpoint(namespace=dynamic, schema=Realm)
def realm(*, realmSlug):
    return f"/data/wow/realm/{realmSlug}"
# def realm_search


@endpoint(namespace=dynamic)
def region_index():
    return f"/data/wow/region/index"


@endpoint(namespace=dynamic)
def region(*, regionId):
    return f"/data/wow/region/{regionId}"


@endpoint(namespace=static)
def spell(*, spellId):
    return f"/data/wow/spell/{spellId}"


@endpoint(namespace=static)
def spell_media(*, spellId):
    return f"/data/wow/media/spell/{spellId}"
# spell-search


@endpoint(namespace=profile)
def character_achievement(*, realmSlug, characterName):
    return f"/profile/wow/character/{realmSlug}/{characterName}/achievements"


@endpoint(namespace=profile)
def character_achievement_statistics(*, realmSlug, characterName):
    return f"/profile/wow/character/{realmSlug}/{characterName}/achievements/statistics"


@endpoint(namespace=profile)
def character_appearance(*, realmSlug, characterName):
    return f"/profile/wow/character/{realmSlug}/{characterName}/appearance"


@endpoint(namespace=profile)
def character_collection_index(*, realmSlug, characterName):
    return f"/profile/wow/character/{realmSlug}/{characterName}/collections"


@endpoint(namespace=profile)
def character_collection_mount(*, realmSlug, characterName):
    return f"/profile/wow/character/{realmSlug}/{characterName}/collections/mounts"


@endpoint(namespace=profile)
def character_collection_pet(*, realmSlug, characterName):
    return f"/profile/wow/character/{realmSlug}/{characterName}/collections/pets"


@endpoint(namespace=profile)
def character_media(*, realmSlug, characterName):
    return f"/profile/wow/character/{realmSlug}/{characterName}/character-media"


@endpoint(namespace=profile)
def character_statistics(*, realmSlug, characterName):
    return f"/profile/wow/character/{realmSlug}/{characterName}/statistics"


@endpoint(namespace=profile)
def character_titles(*, realmSlug, characterName):
    return f"/profile/wow/character/{realmSlug}/{characterName}/titles"
