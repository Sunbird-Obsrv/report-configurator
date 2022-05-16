# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""add_static_interval_to_hawkeye_chart

Revision ID: bf1ec80c8c9a
Revises: 9f2594aee0c4
Create Date: 2020-05-21 13:51:12.240498

"""

# revision identifiers, used by Alembic.
revision = 'bf1ec80c8c9a'
down_revision = '9f2594aee0c4'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    op.add_column('hawkeye_reports', sa.Column('static_interval', sa.Boolean(), default=False))


def downgrade():
    op.drop_column('hawkeye_reports', 'static_interval')