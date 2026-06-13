Archive Test Files
===

本项目内含多格式测试压缩包样本，用于验证目录穿越漏洞利用场景，同时还添加了更多压缩文件示例；项目基于 [jwilk/traversal-archives](https://github.com/jwilk/traversal-archives) 改造，适配 **macOS** 系统正常运行。

```bash
make -C 7zip
make -C ar
make -C arc
make -C arj
make -C cab
make -C rar
make -C tar
make -C zip
make -C zoo
```

## License

MIT © [Kenny Wang](https://wangchujiang.com)
