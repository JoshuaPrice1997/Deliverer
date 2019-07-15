# Deliverer
Map:
A text file indicating the layout of roads and buildings once the game is loaded
Is assumed to be surrounded by zeros (indicating the edge of the map)

Textures:
the tiles text file is used by the code when loading texture files, modifying this txt will cause errors
the "tiles_inteded" txt is a list of tiles that I intend to make as they will be neccessary for the game. Once these textures are made, the names will be moved from the intentional file to the actual file.
"blank" indicates a texture tile does not exist, however it is neccessary for its index to exist in case the map is intiialised incorrectly and the function tileChekcer() attempts to access a tile with that index
The indices are as such, the first digit indicates the type, currently: 0 for edges, 1 for roads and 2 for buildings.
THe second digit indicates its direction, i.e. the amount adjacent spaces that are of the same type. For instance, rd_124 is a t-junction, a road where the south, east and west sides are also roads, the first, second and fourht directions respectively.

    3
    |
2 --+--4

    |
    1
