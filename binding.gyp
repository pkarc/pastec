{
    "targets": [{
        "target_name": "pastec",
        "sources": [
            "src/node.cpp",
            "src/imageloader.cpp",
            "src/imagereranker.cpp",
            "src/imagererankerransac.cpp",
            "src/orb/orbfeatureextractor.cpp",
            "src/orb/orbindex.cpp",
            "src/orb/orbwordindex.cpp",
            "src/orb/orbsearcher.cpp",
        ],
        "libraries": [
            "<!@(pkg-config --libs opencv)"
        ],
        "include_dirs": [
            "src/orb",
            "include",
            "include/orb"
        ],
        "cflags!" : [ "-fno-exceptions"],
        "cflags_cc!": [ "-fno-rtti",  "-fno-exceptions"]
    }]
}
