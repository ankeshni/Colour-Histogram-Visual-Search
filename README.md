# Colour-Histogram-Visual-Search

### Steps to use:

1.Add your Images to Images Folder

2.Index your images by running:

    python index.py --dataset images --index index.cpickle

3.Add your query Images to Query Folder: 

    python search.py --dataset images --index index.cpickle
    
### Use The following command for analysis on quality of your indexed image dataset
  
    python search_external.py --dataset images --index index.cpickle --query queries/Img.png

