# tools/site_summary.py
import json
from datetime import datetime
from typing import List, Dict, Any


# ----------------------------------------------------------------
# 站点资料数据集（内置静态数据，无需网络）
# ----------------------------------------------------------------
SITE_DATABASE: List[Dict[str, Any]] = [
    {
        "id": "s001",
        "title": "爱游戏门户",
        "url": "https://site-index-aiyouxi.com.cn",
        "keywords": ["爱游戏", "游戏门户", "游戏资讯"],
        "tags": ["游戏", "门户", "中文"],
        "description": "提供海量游戏资讯、评测与活动信息，是游戏爱好者的首选平台。",
        "category": "综合游戏",
        "last_updated": "2024-05-10",
    },
    {
        "id": "s002",
        "title": "爱游戏攻略站",
        "url": "https://site-index-aiyouxi.com.cn/guides",
        "keywords": ["爱游戏攻略", "游戏教程", "攻略指南"],
        "tags": ["攻略", "教程", "爱游戏"],
        "description": "汇集各款热门游戏的详细攻略、技巧与隐藏要素。",
        "category": "攻略",
        "last_updated": "2024-05-08",
    },
    {
        "id": "s003",
        "title": "爱游戏社区",
        "url": "https://site-index-aiyouxi.com.cn/community",
        "keywords": ["爱游戏社区", "玩家交流", "论坛"],
        "tags": ["社区", "论坛", "互动"],
        "description": "玩家自由交流心得、组队、分享同人创作的热情社区。",
        "category": "社区",
        "last_updated": "2024-05-12",
    },
    {
        "id": "s004",
        "title": "爱游戏商城",
        "url": "https://site-index-aiyouxi.com.cn/shop",
        "keywords": ["爱游戏商城", "游戏充值", "道具购买"],
        "tags": ["商城", "充值", "道具"],
        "description": "安全便捷的游戏点卡、虚拟道具与礼包购买平台。",
        "category": "商城",
        "last_updated": "2024-05-09",
    },
]


# ----------------------------------------------------------------
# 辅助函数：格式化单个站点摘要文本
# ----------------------------------------------------------------
def format_site_summary(site: Dict[str, Any], index: int = 1) -> str:
    """将一条站点记录格式化为结构化摘要文本"""
    lines = [
        f"  [{index}] {site['title']}",
        f"       URL     : {site['url']}",
        f"       关键词  : {', '.join(site['keywords'])}",
        f"       标签    : {', '.join(site['tags'])}",
        f"       类别    : {site['category']}",
        f"       说明    : {site['description']}",
        f"       最后更新: {site['last_updated']}",
    ]
    return "\n".join(lines)


# ----------------------------------------------------------------
# 核心函数：生成完整站点摘要报告
# ----------------------------------------------------------------
def generate_site_summary(sites: List[Dict[str, Any]] = None) -> str:
    """
    读取内置站点资料，输出结构化摘要字符串。
    如果未指定 sites，则使用 SITE_DATABASE。
    """
    if sites is None:
        sites = SITE_DATABASE

    if not sites:
        return "（无站点资料）"

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"站点资料摘要（生成时间: {now_str}）"
    separator = "=" * 55
    lines = [
        separator,
        header,
        separator,
        "",
    ]

    for idx, site in enumerate(sites, start=1):
        lines.append(format_site_summary(site, index=idx))
        lines.append("")

    summary_line = f"共收录 {len(sites)} 个站点"
    lines.append(summary_line)
    lines.append(separator)

    return "\n".join(lines)


# ----------------------------------------------------------------
# 额外功能：按关键词或标签搜索站点
# ----------------------------------------------------------------
def search_sites(
    query: str,
    sites: List[Dict[str, Any]] = None,
    search_in: str = "both",
) -> List[Dict[str, Any]]:
    """
    搜索站点数据，返回匹配的记录列表。
    search_in 可选 'keywords', 'tags', 'both'。
    """
    if sites is None:
        sites = SITE_DATABASE

    if not query.strip():
        return sites

    q = query.strip().lower()
    results: List[Dict[str, Any]] = []

    for site in sites:
        match_keywords = any(q in kw.lower() for kw in site["keywords"])
        match_tags = any(q in tag.lower() for tag in site["tags"])

        if search_in == "keywords" and match_keywords:
            results.append(site)
        elif search_in == "tags" and match_tags:
            results.append(site)
        elif search_in == "both" and (match_keywords or match_tags):
            results.append(site)

    return results


# ----------------------------------------------------------------
# 控制台入口：直接运行显示完整摘要
# ----------------------------------------------------------------
if __name__ == "__main__":
    print(generate_site_summary())
    print("\n--- 示例搜索：查询 '社区' ---")
    found = search_sites("社区")
    print(f"匹配 {len(found)} 个站点：")
    for s in found:
        print(f"  - {s['title']} ({s['url']})")