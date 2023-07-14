import random

missions = {1:{1: "Critical Operations - 1.1 $Loot and Salvage$critical-operations",
               2: "Critical Operations - 1.2 $Consecration$critical-operations",
               3: "Critical Operations - 1.3 $Awaken the Data-spirits$critical-operations",
               4: "Critical Operations - 2.1 $Escalating Hostilities$critical-operations",
               5: "Critical Operations - 2.2 $Seize Ground$critical-operations",
               6: "Critical Operations - 2.3 $Domination$critical-operations",
               7: "Critical Operations - 3.1 $Secure Archeotech$critical-operations",
               8: "Critical Operations - 3.2 $Duel of Wits$critical-operations",
               9: "Critical Operations - 3.3 $Master the Terminals$critical-operations"
               },
            2:{1: "Critical Ops: Sentries - 1 $Secure the Approach$critical-ops-sentries",
               2: "Critical Ops: Sentries - 2 $Advance Capture$critical-ops-sentries",
               3: "Critical Ops: Sentries - 3 $Spike Data-core$critical-ops-sentries",
               4: "Critical Ops: Sentries - 4 $Designated Priorities$critical-ops-sentries",
               5: "Critical Ops: Sentries - 5 $Secure Supplies$critical-ops-sentries",
               6: "Critical Ops: Sentries - 6 $Initiate Transmission$critical-ops-sentries"
               },
            3:{1: "Shadow Ops: Last Stand - 1 $Make Your Stand$shadow-ops-last-stand",
               2: "Shadow Ops: Last Stand - 2 $Hold At All Costs$shadow-ops-last-stand",
               3: "Shadow Ops: Last Stand - 3 $Final Transmission$shadow-ops-last-stand" 
               },
            4:{1: "Shadow Ops: The Lure - 1.1 $Relentless Pursuit$shadow-ops-the-lure",
               2: "Shadow Ops: The Lure - 1.2 $Dank Hold$shadow-ops-the-lure",
               3: "Shadow Ops: The Lure - 1.3 $Perilous Morass$shadow-ops-the-lure"
               },
            5:{1: "Shadow Ops: Into The Dark - 1.1 $Reinforced Chamber$into-the-dark",
               2: "Shadow Ops: Into The Dark - 1.2 $Airlocked$into-the-dark",
               3: "Shadow Ops: Into The Dark - 1.3 $Subsidence$into-the-dark",
               4: "Shadow Ops: Into The Dark - 2.1 $Desperate Raid$into-the-dark",
               5: "Shadow Ops: Into The Dark - 2.2 $Deadly Hangar$into-the-dark",
               6: "Shadow Ops: Into The Dark - 2.3 $Maze Breakout$into-the-dark",
               7: "Shadow Ops: Into The Dark - 3.1 $Power Overload$into-the-dark",
               8: "Shadow Ops: Into The Dark - 3.2 $Pursue and Secure$into-the-dark",
               9: "Shadow Ops: Into The Dark - 3.3 $Contact Lost$into-the-dark" 
               },
            6:{1: "Critical Ops: Gallowdark - 1.1 $Command Station Control$into-the-dark",
               2: "Critical Ops: Gallowdark - 1.2 $Power Surge$into-the-dark",
               3: "Critical Ops: Gallowdark - 1.3 $Supply Raid$into-the-dark",
               4: "Critical Ops: Gallowdark - 2.1 $Junction Assault$into-the-dark",
               5: "Critical Ops: Gallowdark - 2.2 $Full-scale Attack$into-the-dark",
               6: "Critical Ops: Gallowdark - 2.3 $Mysterious Signature$into-the-dark",
               7: "Critical Ops: Gallowdark - 3.1 $Forge Stronghold$into-the-dark",
               8: "Critical Ops: Gallowdark - 3.2 $Vault Plunder$into-the-dark",
               9: "Critical Ops: Gallowdark - 3.3 $Exposed Trove$into-the-dark" 
               },
            7:{1: "Shadow Ops: Octarius War - 1.1 $Reconnoitre$octarius",
               2: "Shadow Ops: Octarius War - 1.2 $Search and Retrieve$octarius",
               3: "Shadow Ops: Octarius War - 1.3 $Fuel Run$octarius",
               4: "Shadow Ops: Octarius War - 2.1 $Eliminate Target$octarius",
               5: "Shadow Ops: Octarius War - 2.2 $Saboteurs$octarius",
               6: "Shadow Ops: Octarius War - 2.3 $Supply Drop$octarius",
               7: "Shadow Ops: Octarius War - 3.1 $Ambush$octarius",
               8: "Shadow Ops: Octarius War - 3.2 $Evac Inbound$octarius",
               9: "Shadow Ops: Octarius War - 3.3 $Breach Defences$octarius" 
               },
            8:{1: "Shadow Ops: Chalnath - 1.1 $Secure the Relics$chalnath",
               2: "Shadow Ops: Chalnath - 1.2 $Defend the Position$chalnath",
               3: "Shadow Ops: Chalnath - 1.3 $Escort$chalnath",
               4: "Shadow Ops: Chalnath - 2.1 $Retrieve Information$chalnath",
               5: "Shadow Ops: Chalnath - 2.2 $Sensor Grid$chalnath",
               6: "Shadow Ops: Chalnath - 2.3 $Spread the Word$chalnath",
               7: "Shadow Ops: Chalnath - 3.1 $Launch Strike$chalnath",
               8: "Shadow Ops: Chalnath - 3.2 $Destroy Foundations$chalnath",
               9: "Shadow Ops: Chalnath - 3.3 $Exemplar$chalnath" 
               },
            9:{1: "Shadow Ops: Nachmund - 1.1 $Steal the Ciphers$nachmund",
               2: "Shadow Ops: Nachmund - 1.2 $Scavenging the Wreckage$nachmund",
               3: "Shadow Ops: Nachmund - 1.3 $Recover Wreckage$nachmund",
               4: "Shadow Ops: Nachmund - 2.1 $Escape Drill Site$nachmund",
               5: "Shadow Ops: Nachmund - 2.2 $Blow the Reactor$nachmund",
               6: "Shadow Ops: Nachmund - 2.3 $Maze Breakout$nachmund",
               7: "Shadow Ops: Nachmund - 3.1 $Power Overload$nachmund",
               8: "Shadow Ops: Nachmund - 3.2 $Pursue and Secure$nachmund",
               9: "Shadow Ops: Nachmund - 3.3 $Contact Lost$nachmund" 
               },
            10:{1: "Shadow Ops: Moroch - 1.1 $Plunder$moroch",
               2: "Shadow Ops: Moroch - 1.2 $Control the Outpost$moroch",
               3: "Shadow Ops: Moroch - 1.3 $Compound Assault$moroch",
               4: "Shadow Ops: Moroch - 2.1 $Emergency Transmission$moroch",
               5: "Shadow Ops: Moroch - 2.2 $Outrun the Storm$moroch",
               6: "Shadow Ops: Moroch - 2.3 $Smoking Ruin$moroch",
               7: "Shadow Ops: Moroch - 3.1 $Demolitions$moroch",
               8: "Shadow Ops: Moroch - 3.2 $Infiltrate the Landing Pad$moroch",
               9: "Shadow Ops: Moroch - 3.3 $Stealth Offensive$moroch" 
               },
            11:{1: "Shadow Ops: Shadowvaults - 1.1 $Deadly Juncture$shadowvaults",
               2: "Shadow Ops: Shadowvaults - 1.2 $Passageway of Death$shadowvaults",
               3: "Shadow Ops: Shadowvaults - 1.3 $Uncover Riches$shadowvaults",
               4: "Shadow Ops: Shadowvaults - 2.1 $Demolition Run$shadowvaults",
               5: "Shadow Ops: Shadowvaults - 2.2 $Storm the Vault$shadowvaults",
               6: "Shadow Ops: Shadowvaults - 2.3 $Hold Out$shadowvaults",
               7: "Shadow Ops: Shadowvaults - 3.1 $Secure Base$shadowvaults",
               8: "Shadow Ops: Shadowvaults - 3.2 $Covert Attack$shadowvaults",
               9: "Shadow Ops: Shadowvaults - 3.3 $Lightning Raid$shadowvaults" 
               },
            12:{1: "Shadow Ops: Soulshackle - 1.1 $Inload Data-gheist$soulshackle",
               2: "Shadow Ops: Soulshackle - 1.2 $Awaken Control Cores$soulshackle",
               3: "Shadow Ops: Soulshackle - 1.3 $Cryptogrammic Raid$soulshackle",
               4: "Shadow Ops: Soulshackle - 2.1 $Reignite Comms$soulshackle",
               5: "Shadow Ops: Soulshackle - 2.2 $Bridge Assault$soulshackle",
               6: "Shadow Ops: Soulshackle - 2.3 $Command Centre Surrounded$soulshackle",
               7: "Shadow Ops: Soulshackle - 3.1 $Service Tunnels$soulshackle",
               8: "Shadow Ops: Soulshackle - 3.2 $Hasty Defence$soulshackle",
               9: "Shadow Ops: Soulshackle - 3.3 $Recover Archives$soulshackle" 
               }  
               }

# This is for testing purposes:
miss_list = []
for i in range(1,13):
    if i == 2:
        miss_2_test = 0
        for j in range(1,7):
            miss_name = missions[i][j].split("$")
            miss_list.append(f"Mission selcted: {miss_name[0]}Link: https://wahapedia.ru/kill-team2/the-rules/{miss_name[2]}/#{miss_name[1].replace(' ', '-')}")
            miss_2_test += 1
        if miss_2_test == 6:
            print(f"Mission {i} passed")
        else:
            print(f"Mission {i} failed")
            break
    elif i == 3 or i== 4:
        miss_3_4_test = 0
        for j in range(1,4):
            miss_name = missions[i][j].split("$")
            miss_list.append(f"Mission selcted: {miss_name[0]}Link: https://wahapedia.ru/kill-team2/the-rules/{miss_name[2]}/#{miss_name[1].replace(' ', '-')}")
            miss_3_4_test += 1
        if miss_3_4_test == 3:
            print(f"Mission {i} passed")
        else:
            print(f"Mission {i} failed")
            break
    else:
        miss_test = 0 
        for j in range(1,10):
            miss_name = missions[i][j].split("$")
            miss_list.append(f"Mission selcted: {miss_name[0]}Link: https://wahapedia.ru/kill-team2/the-rules/{miss_name[2]}/#{miss_name[1].replace(' ', '-')}")
            miss_test += 1
        if miss_test == 9:
            print(f"Mission {i} passed")
        else:
            print(f"Mission {i} failed")
            break
print(len(miss_list))
if len(miss_list) == 93:
    print(f"All {len(miss_list)} missions accounted for.")
else:
    print(f"Missing missions. Total missions: {len(miss_list)}. Missing {93 - len(miss_list)}.")
    for i in range(len(miss_list)):
        print(f"Missions in list:{miss_list[i]}")

first = random.randrange(1,13)
if first == 2:
    second = random.randrange(1,7)
elif first == 3 or first == 4:
     second = random.randrange(1,4)
else:
    second = random.randrange(1,10)
print(f"first number: {first}\nsecond number: {second}")
miss_name = missions[first][second].split("$")
print(f"Mission selected: {miss_name[0]}{miss_name[1]} \nLink: https://wahapedia.ru/kill-team2/the-rules/{miss_name[2]}/#{miss_name[1].replace(' ', '-')}")