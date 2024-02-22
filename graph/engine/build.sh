# thank you so much Surma.
# https://surma.dev/things/c-to-webassembly/

 clang \
   --target=wasm32 \
   -O3 \
   -flto \
   -nostdlib \
   -Wl,--no-entry \
   -Wl,--export-all \
   -Wl,--lto-O3 \
  -Wl,-z,stack-size=$[8 * 1024] \
   -o app.wasm \
   app.c

