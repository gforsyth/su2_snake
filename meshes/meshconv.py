def pullnum(str_with_nums):
    '''
    returns a list of all numbers contained in string
    '''

    l = []
    for t in str_with_nums.split():
        try:
            l.append(float(t))
        except ValueError:
            pass

    return l

def addlines(data):
    numpoints = len(data)+1
    for i in xrange(1,numpoints):
        linestr = 'Line({}) = {{{}, {}}};'.format(i, i, i+1)
        data.append(linestr)

    linestr = 'Line({}) = {{{}, {}}};'.format(numpoints, numpoints, 1)
    data.append(linestr)

    return data

def writelist2file(data):
    with open('meshout.geo','w') as f:
        for row in data:
            f.write(row)
            f.write('\n')

def main():
    file = open('flyingSnake_AOA25_coordinates.obj','r')

    lines = file.readlines()

    numpoints = [int(s) for s in lines[1].split() if s.isdigit()][0]

    meshpoints = []
    pointnum = 1

    for i in lines[5:numpoints+5]:
        point_coords = pullnum(i)
        
        if point_coords[-1] == 0:
            coord_str = 'Point ({}) = {{ {}, {}, {}, 1e+22}};'.\
                    format(pointnum, point_coords[0], point_coords[1], point_coords[2])
            meshpoints.append(coord_str)
            pointnum += 1

    meshpoints = addlines(meshpoints)
    
    writelist2file(meshpoints)
