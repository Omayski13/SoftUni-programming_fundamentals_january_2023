while True:
    line = input()
    quntity, input_materials = line.split(" ")
    materials = {}
    # legendary_materials = {"shards": "Shadowmourne", "fragments":"Valanyr", "motes":"Dragonwrath"}
    # for index in range(0, len(input_materials) - 1, 2):
    #     if input_materials[index+1] not in materials:
    #         materials[input_materials[index+1]] = int(input_materials[index])
    #     else:
    #         materials[input_materials[index + 1]] += int(input_materials[index])
    #
    #     for material in legendary_materials.keys():
    #         if material in materials and materials[material] >= 250:
    #             print(f"{legendary_materials[material]} obtained!")
    #             break






print(materials)


