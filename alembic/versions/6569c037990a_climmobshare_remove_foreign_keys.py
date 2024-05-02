"""climmobShare - Remove Foreign Keys

Revision ID: 6569c037990a
Revises: 7d3931b8745e
Create Date: 2021-08-09 15:28:28.342991

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "6569c037990a"
down_revision = "7d3931b8745e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("fk_assessment_asssection1_idx", table_name="assdetail")
    op.drop_constraint(
        "fk_assdetail_user_name_assessment", "assdetail", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_assdetail_section_user_asssection", "assdetail", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_assdetail_question_id_question", "assdetail", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_assesment_jsonlog_enum_user_enumerator",
        "assesment_jsonlog",
        type_="foreignkey",
    )
    op.drop_constraint(
        "fk_assesment_jsonlog_user_name_assessment",
        "assesment_jsonlog",
        type_="foreignkey",
    )
    op.drop_constraint(
        "fk_assessment_user_name_project", "assessment", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_asssection_user_name_assessment", "asssection", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_i18n_asssection_user_name_asssection", "i18n_asssection", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_i18n_asssection_lang_code_i18n", "i18n_asssection", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_i18n_prjalias_prjalias1", "i18n_prjalias", type_="foreignkey"
    )
    op.drop_constraint("fk_i18n_prjalias_i18n1", "i18n_prjalias", type_="foreignkey")
    op.drop_constraint("fk_i18n_project_i18n1", "i18n_project", type_="foreignkey")
    op.drop_constraint("fk_i18n_project_project1", "i18n_project", type_="foreignkey")
    op.drop_constraint("fk_i18n_question_i18n1", "i18n_question", type_="foreignkey")
    op.drop_constraint(
        "fk_i18n_regsection_i18n1", "i18n_regsection", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_i18n_regsection_regsection1", "i18n_regsection", type_="foreignkey"
    )
    op.drop_constraint("fk_package_project1", "package", type_="foreignkey")
    op.drop_constraint("fk_pkgcomb_package1", "pkgcomb", type_="foreignkey")
    op.drop_constraint("fk_pkgcomb_prjcombination1", "pkgcomb", type_="foreignkey")
    op.drop_index("fk_prjalias_prjtech1_idx", table_name="prjalias")
    op.drop_constraint("fk_prjalias_techalias1", "prjalias", type_="foreignkey")
    op.drop_constraint("fk_prjalias_prjtech1", "prjalias", type_="foreignkey")
    op.drop_constraint("fk_prjcnty_country1", "prjcnty", type_="foreignkey")
    op.drop_constraint("fk_prjcnty_project1", "prjcnty", type_="foreignkey")
    op.drop_constraint("fk_prjcombdet_prjalias1", "prjcombdet", type_="foreignkey")
    op.drop_constraint(
        "fk_prjcombdet_prjcombination1", "prjcombdet", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_prjcombination_project1", "prjcombination", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_prjenumerator_enum_user_enumerator", "prjenumerator", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_prjenumerator_user_name_project", "prjenumerator", type_="foreignkey"
    )
    op.drop_constraint("fk_prjlang_i18n1", "prjlang", type_="foreignkey")
    op.drop_constraint("fk_prjlang_project1", "prjlang", type_="foreignkey")
    op.drop_constraint("fk_prjtech_technology1", "prjtech", type_="foreignkey")
    op.drop_constraint("fk_prjtech_project1", "prjtech", type_="foreignkey")
    op.drop_constraint("fk_products_user_name_project", "products", type_="foreignkey")
    op.drop_constraint("fk_project_project_cnty_country", "project", type_="foreignkey")
    op.drop_constraint("fk_project_user1", "project", type_="foreignkey")
    op.drop_constraint("fk_registry_project1", "registry", type_="foreignkey")
    op.drop_constraint("fk_registry_question1", "registry", type_="foreignkey")
    op.drop_constraint("fk_registry_regsection1", "registry", type_="foreignkey")
    op.drop_constraint(
        "fk_registry_jsonlog_user_name_project", "registry_jsonlog", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_registry_jsonlog_enum_user_enumerator",
        "registry_jsonlog",
        type_="foreignkey",
    )
    op.drop_constraint("fk_regsection_project1", "regsection", type_="foreignkey")
    op.drop_constraint(
        "fk_storageerrors_user_name_project", "storageerrors", type_="foreignkey"
    )
    op.drop_index("fk_pkgcomb_prjcombination1_idx", table_name="pkgcomb")
    op.drop_index("fk_prjalias_techalias1_idx", table_name="prjalias")
    op.drop_index("fk_prjcombdet_prjalias1_idx", table_name="prjcombdet")
    op.drop_index("fk_registry_regsection1_idx", table_name="registry")

    op.drop_index("fk_assdetail_section_user_asssection", table_name="assdetail")
    op.drop_index(
        "fk_assesment_jsonlog_enum_user_enumerator", table_name="assesment_jsonlog"
    )
    op.drop_index("fk_prjenumerator_enum_user_enumerator", table_name="prjenumerator")
    op.drop_index("fk_products_user_name_project", table_name="products")
    op.drop_index(
        "fk_registry_jsonlog_enum_user_enumerator", table_name="registry_jsonlog"
    )
    op.drop_index("fk_storageerrors_user_name_project", table_name="storageerrors")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        "fk_storageerrors_user_name_project",
        "storageerrors",
        ["user_name", "project_cod"],
        unique=False,
    )
    op.create_index(
        "fk_registry_jsonlog_enum_user_enumerator",
        "registry_jsonlog",
        ["enum_user", "enum_id"],
        unique=False,
    )
    op.create_index(
        "fk_products_user_name_project",
        "products",
        ["user_name", "project_cod"],
        unique=False,
    )
    op.create_index(
        "fk_prjenumerator_enum_user_enumerator",
        "prjenumerator",
        ["enum_user", "enum_id"],
        unique=False,
    )
    op.create_index(
        "fk_assesment_jsonlog_enum_user_enumerator",
        "assesment_jsonlog",
        ["enum_user", "enum_id"],
        unique=False,
    )
    op.create_index(
        "fk_assdetail_section_user_asssection",
        "assdetail",
        ["section_user", "section_project", "section_assessment", "section_id"],
        unique=False,
    )

    op.create_index(
        "fk_registry_regsection1_idx",
        "registry",
        ["section_user", "section_project", "section_id"],
        unique=False,
    )
    op.create_index(
        "fk_prjcombdet_prjalias1_idx",
        "prjcombdet",
        ["user_name", "project_cod", "tech_id", "alias_id"],
        unique=False,
    )
    op.create_index(
        "fk_prjalias_techalias1_idx",
        "prjalias",
        ["tech_used", "alias_used"],
        unique=False,
    )
    op.create_index(
        "fk_pkgcomb_prjcombination1_idx",
        "pkgcomb",
        ["comb_user", "comb_project", "comb_code"],
        unique=False,
    )
    op.create_foreign_key(
        "fk_storageerrors_user_name_project",
        "storageerrors",
        "project",
        ["user_name", "project_cod"],
        ["user_name", "project_cod"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_regsection_project1",
        "regsection",
        "project",
        ["user_name", "project_cod"],
        ["user_name", "project_cod"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_registry_jsonlog_enum_user_enumerator",
        "registry_jsonlog",
        "enumerator",
        ["enum_user", "enum_id"],
        ["user_name", "enum_id"],
    )
    op.create_foreign_key(
        "fk_registry_jsonlog_user_name_project",
        "registry_jsonlog",
        "project",
        ["user_name", "project_cod"],
        ["user_name", "project_cod"],
    )
    op.create_foreign_key(
        "fk_registry_regsection1",
        "registry",
        "regsection",
        ["section_user", "section_project", "section_id"],
        ["user_name", "project_cod", "section_id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_registry_question1",
        "registry",
        "question",
        ["question_id"],
        ["question_id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_registry_project1",
        "registry",
        "project",
        ["user_name", "project_cod"],
        ["user_name", "project_cod"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_project_user1", "project", "user", ["user_name"], ["user_name"]
    )
    op.create_foreign_key(
        "fk_project_project_cnty_country",
        "project",
        "country",
        ["project_cnty"],
        ["cnty_cod"],
    )
    op.create_foreign_key(
        "fk_products_user_name_project",
        "products",
        "project",
        ["user_name", "project_cod"],
        ["user_name", "project_cod"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_prjtech_project1",
        "prjtech",
        "project",
        ["user_name", "project_cod"],
        ["user_name", "project_cod"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_prjtech_technology1",
        "prjtech",
        "technology",
        ["tech_id"],
        ["tech_id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_prjlang_project1",
        "prjlang",
        "project",
        ["user_name", "project_cod"],
        ["user_name", "project_cod"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_prjlang_i18n1",
        "prjlang",
        "i18n",
        ["lang_code"],
        ["lang_code"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_prjenumerator_user_name_project",
        "prjenumerator",
        "project",
        ["user_name", "project_cod"],
        ["user_name", "project_cod"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_prjenumerator_enum_user_enumerator",
        "prjenumerator",
        "enumerator",
        ["enum_user", "enum_id"],
        ["user_name", "enum_id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_prjcombination_project1",
        "prjcombination",
        "project",
        ["user_name", "project_cod"],
        ["user_name", "project_cod"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_prjcombdet_prjcombination1",
        "prjcombdet",
        "prjcombination",
        ["prjcomb_user", "prjcomb_project", "comb_code"],
        ["user_name", "project_cod", "comb_code"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_prjcombdet_prjalias1",
        "prjcombdet",
        "prjalias",
        ["user_name", "project_cod", "tech_id", "alias_id"],
        ["user_name", "project_cod", "tech_id", "alias_id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_prjcnty_project1",
        "prjcnty",
        "project",
        ["user_name", "project_cod"],
        ["user_name", "project_cod"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_prjcnty_country1",
        "prjcnty",
        "country",
        ["cnty_cod"],
        ["cnty_cod"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_prjalias_prjtech1",
        "prjalias",
        "prjtech",
        ["user_name", "project_cod", "tech_id"],
        ["user_name", "project_cod", "tech_id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_prjalias_techalias1",
        "prjalias",
        "techalias",
        ["tech_used", "alias_used"],
        ["tech_id", "alias_id"],
        ondelete="CASCADE",
    )
    op.create_index(
        "fk_prjalias_prjtech1_idx",
        "prjalias",
        ["user_name", "project_cod", "tech_id"],
        unique=False,
    )
    op.create_foreign_key(
        "fk_pkgcomb_prjcombination1",
        "pkgcomb",
        "prjcombination",
        ["comb_user", "comb_project", "comb_code"],
        ["user_name", "project_cod", "comb_code"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_pkgcomb_package1",
        "pkgcomb",
        "package",
        ["user_name", "project_cod", "package_id"],
        ["user_name", "project_cod", "package_id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_package_project1",
        "package",
        "project",
        ["user_name", "project_cod"],
        ["user_name", "project_cod"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_i18n_regsection_regsection1",
        "i18n_regsection",
        "regsection",
        ["user_name", "project_cod", "section_id"],
        ["user_name", "project_cod", "section_id"],
    )
    op.create_foreign_key(
        "fk_i18n_regsection_i18n1",
        "i18n_regsection",
        "i18n",
        ["lang_code"],
        ["lang_code"],
    )
    op.create_foreign_key(
        "fk_i18n_question_i18n1", "i18n_question", "i18n", ["lang_code"], ["lang_code"]
    )
    op.create_foreign_key(
        "fk_i18n_project_project1",
        "i18n_project",
        "project",
        ["user_name", "project_cod"],
        ["user_name", "project_cod"],
    )
    op.create_foreign_key(
        "fk_i18n_project_i18n1", "i18n_project", "i18n", ["lang_code"], ["lang_code"]
    )
    op.create_foreign_key(
        "fk_i18n_prjalias_i18n1", "i18n_prjalias", "i18n", ["lang_code"], ["lang_code"]
    )
    op.create_foreign_key(
        "fk_i18n_prjalias_prjalias1",
        "i18n_prjalias",
        "prjalias",
        ["user_name", "project_cod", "tech_id", "alias_id"],
        ["user_name", "project_cod", "tech_id", "alias_id"],
    )
    op.create_foreign_key(
        "fk_i18n_asssection_lang_code_i18n",
        "i18n_asssection",
        "i18n",
        ["lang_code"],
        ["lang_code"],
    )
    op.create_foreign_key(
        "fk_i18n_asssection_user_name_asssection",
        "i18n_asssection",
        "asssection",
        ["user_name", "project_cod", "ass_cod", "section_id"],
        ["user_name", "project_cod", "ass_cod", "section_id"],
    )
    op.create_foreign_key(
        "fk_asssection_user_name_assessment",
        "asssection",
        "assessment",
        ["user_name", "project_cod", "ass_cod"],
        ["user_name", "project_cod", "ass_cod"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_assessment_user_name_project",
        "assessment",
        "project",
        ["user_name", "project_cod"],
        ["user_name", "project_cod"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_assesment_jsonlog_user_name_assessment",
        "assesment_jsonlog",
        "assessment",
        ["user_name", "project_cod", "ass_cod"],
        ["user_name", "project_cod", "ass_cod"],
    )
    op.create_foreign_key(
        "fk_assesment_jsonlog_enum_user_enumerator",
        "assesment_jsonlog",
        "enumerator",
        ["enum_user", "enum_id"],
        ["user_name", "enum_id"],
    )
    op.create_foreign_key(
        "fk_assdetail_question_id_question",
        "assdetail",
        "question",
        ["question_id"],
        ["question_id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_assdetail_section_user_asssection",
        "assdetail",
        "asssection",
        ["section_user", "section_project", "section_assessment", "section_id"],
        ["user_name", "project_cod", "ass_cod", "section_id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_assdetail_user_name_assessment",
        "assdetail",
        "assessment",
        ["user_name", "project_cod", "ass_cod"],
        ["user_name", "project_cod", "ass_cod"],
        ondelete="CASCADE",
    )
    op.create_index(
        "fk_assessment_asssection1_idx",
        "assdetail",
        ["section_user", "section_project", "section_id"],
        unique=False,
    )
    # ### end Alembic commands ###
