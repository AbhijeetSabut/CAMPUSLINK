from fastapi import APIRouter
from analytics.src.placement_analysis import get_placement_analysis
from analytics.src.company_analysis import get_company_analysis
from analytics.src.job_demand import get_job_demand
from analytics.src.skill_analysis import get_skill_analysis
from analytics.src.student_readiness import get_student_readiness

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/placement")
def placement():
    return get_placement_analysis()


@router.get("/companies")
def companies():
    return get_company_analysis()


@router.get("/jobs")
def jobs():
    return get_job_demand()


@router.get("/skills")
def skills():
    return get_skill_analysis()


@router.get("/student-readiness")
def student_readiness():
    return get_student_readiness()