
# SDL – Secure Deletion

`SDL` is a small Python-based tool (wrapped in `sdl.bat`) that securely deletes files and folders by overwriting their contents before removal.

## Usage

```bash
sdl <path> [options]
```

## Options
  
-r : Recursively delete a folder and its contents.  
-p N : Number of overwrite passes (default = 3).  

## Notes

Multiple passes add redundancy, but even 1 pass is usually enough on modern drives.  
On SSDs, full irrecoverability can’t be guaranteed due to wear-leveling.  
