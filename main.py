DATA = {

    "BRO": {

        "BSN": { "W": 10, "L": 12 },

        "CHC": { "W": 15, "L": 7 },

        "CIN": { "W": 15, "L": 7 },

        "NYG": { "W": 14, "L": 8 },

        "PHI": { "W": 14, "L": 8 },

        "PIT": { "W": 15, "L": 7 },

        "STL": { "W": 11, "L": 11 }

    },

    "BSN": {

        "BRO": { "W": 12, "L": 10 },

        "CHC": { "W": 13, "L": 9 },

        "CIN": { "W": 13, "L": 9 },

        "NYG": { "W": 13, "L": 9 },

        "PHI": { "W": 14, "L": 8 },

        "PIT": { "W": 12, "L": 10 },

        "STL": { "W": 9, "L": 13 }

    },

    "CHC": {

        "BRO": { "W": 7, "L": 15 },

        "BSN": { "W": 9, "L": 13 },

        "CIN": { "W": 12, "L": 10 },

        "NYG": { "W": 7, "L": 15 },

        "PHI": { "W": 16, "L": 6 },

        "PIT": { "W": 8, "L": 14 },

        "STL": { "W": 10, "L": 12 }

    },

    "CIN": {

        "BRO": { "W": 7, "L": 15 },

        "BSN": { "W": 9, "L": 13 },

        "CHC": { "W": 10, "L": 12 },

        "NYG": { "W": 13, "L": 9 },

        "PHI": { "W": 13, "L": 9 },

        "PIT": { "W": 13, "L": 9 },

        "STL": { "W": 8, "L": 14 }

    },

    "NYG": {

        "BRO": { "W": 8, "L": 14 },

        "BSN": { "W": 9, "L": 13 },

        "CHC": { "W": 15, "L": 7 },

        "CIN": { "W": 9, "L": 13 },

        "PHI": { "W": 12, "L": 10 },

        "PIT": { "W": 15, "L": 7 },

        "STL": { "W": 13, "L": 9 }

    },

    "PHI": {

        "BRO": { "W": 8, "L": 14 },

        "BSN": { "W": 8, "L": 14 },

        "CHC": { "W": 6, "L": 16 },

        "CIN": { "W": 9, "L": 13 },

        "NYG": { "W": 10, "L": 12 },

        "PIT": { "W": 13, "L": 9 },

        "STL": { "W": 8, "L": 14 }

    },

    "PIT": {

        "BRO": { "W": 7, "L": 15 },

        "BSN": { "W": 10, "L": 12 },

        "CHC": { "W": 14, "L": 8 },

        "CIN": { "W": 9, "L": 13 },

        "NYG": { "W": 7, "L": 15 },

        "PHI": { "W": 9, "L": 13 },

        "STL": { "W": 6, "L": 16 }

    },

    "STL": {

        "BRO": { "W": 11, "L": 11 },

        "BSN": { "W": 13, "L": 9 },

        "CHC": { "W": 12, "L": 10 },

        "CIN": { "W": 14, "L": 8 },

        "NYG": { "W": 9, "L": 13 },

        "PHI": { "W": 14, "L": 8 },

        "PIT": { "W": 16, "L": 6 }

    }

}

def main():
    count = 0 #used for labeling purposes
    for key in DATA:
        count += 1
        if count == 1:
            longest = printLabels()
        
        x = DATA.get(key)
        print(" " * (longest - len(key)) + key + " |", end='')
    
        for i in DATA: 
            try:
                wins = str( x.get(i).get("W") ) 

                #right align the values 
                print(" " * (len(i) - len(wins)) + wins + "|", end='')
            except: #i == key -> same team
                print(" " * (len(i) - 2) + "--|", end='')
        print("")

        if(count == len(DATA)):
            printLabels()

def printLabels():
    '''A function to create the top/bottom team labels. Makes sure labels are aligned regardless of length. 

    Args: 
        
    Returns: 
        longest: int representing the length of the longest label'''

    longest = 0 
    #print(" Tm |", end='')
    for i in DATA: 
        #print(i + "|", end='')
        if( len(i) > longest ):
            longest = len(i)    # need to know the longest label
                                # before printing the first label
    print(" " * (longest - 2) + "Tm |", end='')
    for i in DATA:
        print(i + "|", end='')
    print("")
    return longest

if __name__ == "__main__":
    main()