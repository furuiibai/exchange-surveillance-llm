from src.schema import SuspiciousCase
from src.features import extract_all_features
from src.prompt_builder import build_full_messages
from src.generator import ReportGenerator, MockGenerator
from src.validators import validate_report
from src.render import save_markdown_report

def run_pipeline(case: SuspiciousCase, output_md_path: str, use_mock: bool = True, api_key: str = None):
    # 1. 提取特征
    feat = extract_all_features(case)
    case_dict = case.model_dump()

    # 2. 组装prompt
    msg = build_full_messages(case_dict, feat)

    # 3. 生成报告
    if use_mock:
        gen = MockGenerator()
    else:
        if not api_key:
            raise ValueError("Need api key when mock=False")
        gen = ReportGenerator(api_key=api_key)
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
    # 这里是本地调试入口，后面可以放sample case
    print("Pipeline ready. Load case and run.")

