def run_pipeline(case: SuspiciousCase, output_md_path: str):
    # 1. 提取特征
    feat = extract_all_features(case)
    case_dict = case.model_dump()
    # 2. 组装模型输入（特征、案件信息打包，后续送入自研模型）
    msg = build_full_messages(case_dict, feat)
    # 3. 自研模型生成报告
    gen = ReportGenerator()
    report = gen.generate_report_markdown(msg)
    # 4. 核心校验：防止数字幻觉
    ok, msg_check = validate_report(report, feat)
    print(f"Validation result: {msg_check}")
    if not ok:
        raise RuntimeError(f"Report failed numeric validation: {msg_check}")
    # 5. 落地保存md报告
    save_markdown_report(report, output_md_path)
    print(f"Report saved to {output_md_path}")
    return report


if __name__ == "__main__":
    print("Pipeline ready. Load case and run.")
    # case = SuspiciousCase(...)  # 在这里构造测试样本
    # run_pipeline(case, "examples/spoofing/report.md")
