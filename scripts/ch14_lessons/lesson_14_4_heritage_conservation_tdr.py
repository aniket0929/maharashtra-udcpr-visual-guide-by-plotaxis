"""
UDCPR Chapter 14 - Lesson 14.4: Conservation of Heritage Buildings, Precincts & Heritage TDR
Statutory Clauses: Regulation 14.5 (14.5.1 to 14.5.12, Appendix-L)
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
    'clause': 'Reg. 14.5 (14.5.1 to 14.5.12)',
    'title': 'Conservation of Heritage Buildings, Precincts & Heritage TDR',
    'meta_desc': 'Master UDCPR Regulation 14.5 for Heritage Conservation: Appendix-L listing process, Grade I (preservation), Grade II (adaptive reuse & harmony), Grade III (townscape character), Heritage Conservation Committee (HCC), skyline covenants, billboard bans, and unconsumed FSI compensation via Heritage TDR.',
    'ch_slug': 'ch14',
    'ch_title': 'Chapter 14: Special Schemes',
    'badge_status': '100% COMPLETE',
    'amendment_cite': 'Statutory Listing & Conservation Guidelines under Appendix-L',
    'filename': 'reg-14-4-heritage-conservation-and-tdr.html',
    'lesson_id': 'ch14_lesson_4',
    'quiz_id': 'quiz_ch14_4',
    'prev_url': '/lessons/reg-14-3-affordable-housing-and-pmay.html',
    'prev_title': 'Reg. 14.3 & 14.4 Affordable Housing & PMAY',
    'next_url': '/lessons/reg-14-5-slum-rehabilitation-schemes.html',
    'next_title': 'Reg. 14.6 & 14.7 Slum Rehabilitation Schemes (SRS)',
    'lead_summary': (
        'To safeguard Maharashtra\'s rich historical legacy, architectural masterpieces, and irreplaceable ecological landmarks from '
        'unrestrained redevelopment, Regulation 14.5 establishes a statutory conservation ecosystem. Covering listed buildings, historic '
        'precincts, sacred groves, and scenic water bodies, the regulation categorizes heritage assets into Grades I, II, and III. '
        'Any modification, repair, or adaptive reuse mandates prior review by the multi-disciplinary Heritage Conservation Committee (HCC). '
        'To prevent economic hardship for private owners who are barred from utilizing full building potential or constructing high-rises, '
        'the UDCPR guarantees financial restitution through Heritage Transferable Development Rights (Heritage TDR), converting unconsumed '
        'development rights into marketable Development Right Certificates (DRC).'
    ),
    'plain_summary_html': """
      <p>
        Regulation 14.5 balances historic preservation with real-estate property rights. It prevents the demolition of landmarks while 
        providing clear economic mechanisms (adaptive reuse and Heritage TDR) so heritage properties do not become financial liabilities:
      </p>
      <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
        <li><strong>Statutory Listing Procedure (Reg 14.5.2 &amp; Appendix-L):</strong>
          <br>&bull; Planning Authorities prepare heritage inventories evaluated on 14 criteria (architectural value, social history, unique craftsmanship, vista significance).
          <br>&bull; Each asset is documented on an authenticated <strong>Heritage List Card (Appendix-L)</strong> by a certified conservation architect.
          <br>&bull; A <strong>30-day public notice</strong> invites objections before submission to the State Government for final gazetting. (Modifications do not require MRTP Section 37/20 procedures).
        </li>
        <li><strong>Three-Tier Statutory Grading System (Reg 14.5.8):</strong>
          <br>&bull; <em>Grade I (National / Prime Importance):</em> Prime landmarks of national or historic excellence (e.g., iconic forts, colonial civic halls). <strong>Careful Preservation</strong>: No exterior or interior interventions permitted except essential structural strengthening using like-to-like materials. Surrounding high-rises barred.
          <br>&bull; <em>Grade II (Regional Importance):</em> Prominent regional landmarks with special architectural or aesthetic merit. <strong>Intelligent Conservation</strong>: Grade II-A permits internal changes and adaptive reuse; Grade II-B permits harmonious extensions/new wings on the same compound.
          <br>&bull; <em>Grade III (Local Townscape Importance):</em> Buildings determining the historic neighborhood character. <strong>Intelligent Conservation</strong>: Internal and external alterations, additions, and adaptive reuses allowed, provided they respect the architectural facade and scale.
        </li>
        <li><strong>Heritage Conservation Committee (HCC) Powers (Reg 14.5.3 &amp; 14.5.10):</strong>
          <br>&bull; Prior written permission of the Authority in consultation with the HCC is mandatory for any repair, painting, or structural change.
          <br>&bull; <em>Non-Delegable Overrule:</em> The Municipal Commissioner can overrule HCC advice only in exceptional circumstances, recording reasons in writing; this power cannot be delegated to subordinate officers.
        </li>
        <li><strong>Heritage TDR Compensation (Reg 14.5.5):</strong>
          <br>&bull; When conservation covenants deprive an owner from consuming the full permissible FSI on the plot, the unconsumed potential is issued as <strong>Heritage TDR (DRC)</strong>, fully tradable across receiving zones.
        </li>
        <li><strong>Skyline Covenants &amp; Billboard Bans (Reg 14.5.6 &amp; 14.5.9):</strong>
          <br>&bull; New surrounding developments must respect the historic skyline, roof profile, and street edge without high-rise overpowering.
          <br>&bull; Commercial outdoor advertising billboards and hoardings are strictly barred on listed heritage buildings and within heritage precincts.
        </li>
      </ul>
    """,
    'statutory_extract': (
        "14.5 CONSERVATION OF HERITAGE BUILDINGS / PRECINCTS / NATURAL FEATURES - No development or redevelopment or engineering operations "
        "or addition, repairs, renovation including painting... shall be allowed except with prior written permission of Authority... "
        "Authority shall consult Heritage Conservation Committee... If owner is deprived of using permissible FSI on said plot... "
        "he shall be entitled for TDR as decided by Authority in consultation with Heritage Conservation Committee."
    ),
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin-top:16px;">
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 14.5.4 // ADAPTIVE REUSE</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">Commercial Incentive Uses</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            To generate maintenance revenue, the Authority in consultation with the HCC may permit conversion of heritage structures 
            into boutique commercial spaces, heritage hotels, museums, or cultural centers, subject to a binding undertaking of ideal upkeep.
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 14.5.10 // MULTI-DISCIPLINARY HCC</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">Committee Composition</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Comprises an independent Government-appointed Chairman, Town Planning officials, ASI and State Archaeology representatives, 
            the local INTACH Convenor, a senior Conservation Architect (&gt;10 yrs exp), and a qualified Historian (&gt;10 yrs exp).
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 14.5.12 // DEDICATED FUND</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">Heritage Conservation Fund</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Local Authorities maintain a dedicated ring-fenced fund fed by municipal budget allocations, voluntary donations, 
            and development cess (up to 0.5%) to provide grants and low-interest loans for urgent private heritage restorations.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="overflow-x:auto; margin-top:12px;">
        <div class="kicker" style="color:var(--blueprint); margin-bottom:6px;">REGULATION 14.5.8 // COMPARATIVE HERITAGE GRADING PLATE</div>
        <table class="blueprint-table" style="width:100%; border-collapse:collapse; font-size:0.88rem;">
          <thead>
            <tr style="background:var(--surface-tint); border-bottom:2px solid var(--line-bold);">
              <th style="padding:10px; text-align:left;">Parameters</th>
              <th style="padding:10px; text-align:left;">Heritage Grade - I</th>
              <th style="padding:10px; text-align:left;">Heritage Grade - II (A &amp; B)</th>
              <th style="padding:10px; text-align:left;">Heritage Grade - III</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>Significance Level</strong></td>
              <td style="padding:10px; color:var(--brick); font-weight:600;">National / Historic Importance</td>
              <td style="padding:10px; color:var(--amber-dark); font-weight:600;">Regional Importance / Local Landmark</td>
              <td style="padding:10px; color:var(--blueprint); font-weight:600;">Local / Townscape Character</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>Core Objective</strong></td>
              <td style="padding:10px;">Careful Preservation</td>
              <td style="padding:10px;">Intelligent Conservation</td>
              <td style="padding:10px;">Intelligent Conservation of Unique Attributes</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>Scope for Change</strong></td>
              <td style="padding:10px;">Strictly no alterations. Only structural strengthening with like-to-like material.</td>
              <td style="padding:10px;">II-A: Internal adaptive reuse allowed under scrutiny.<br>II-B: Harmonious extensions allowed.</td>
              <td style="padding:10px;">Internal &amp; external modifications, adaptive reuse, and harmonious extensions permitted.</td>
            </tr>
            <tr style="border-bottom:2px solid var(--line-bold); background:var(--surface-tint);">
              <td style="padding:10px;"><strong>Surrounding Buffer</strong></td>
              <td style="padding:10px;">Strictly regulated to preserve grandeur &amp; lines of sight. No high-rises.</td>
              <td style="padding:10px;">Skyline and height controlled to harmonize with landmark.</td>
              <td style="padding:10px;">Street facade and height uniformity maintained.</td>
            </tr>
          </tbody>
        </table>
      </div>
    """,
    'worked_example_html': """
      <div style="line-height:1.6; font-size:0.92rem;">
        <h4 style="margin:0 0 8px 0; color:var(--amber-dark);">Scenario: Heritage TDR Calculation for a Grade-II Private Haveli</h4>
        <p>
          A trust owns a listed <strong>Grade-II heritage haveli</strong> situated on a <strong>1,200 sq.m. plot</strong> in a heritage precinct 
          in Chhatrapati Sambhajinagar. The plot abuts a <strong>15-meter road</strong> with a maximum standard building potential of <strong>2.00 FSI</strong> 
          (2,400 sq.m. BUA). The existing historic ground-plus-one structure consumes only <strong>600 sq.m. BUA</strong>. 
          Due to heritage skyline and structural conservation covenants, the HCC prohibits vertical or horizontal expansion. 
          Calculate the Heritage TDR entitlement.
        </p>
        <div style="background:var(--surface); border:1px solid var(--line); padding:12px; margin:10px 0; font-family:var(--mono); font-size:0.85rem;">
          1. Plot Area and Maximum Theoretical Building Potential:<br>
          &nbsp;&nbsp;&bull; Net Plot Area = 1,200 sq.m.<br>
          &nbsp;&nbsp;&bull; Permissible Zone Building Potential (FSI 2.00) = 1,200 &times; 2.00 = <strong>2,400 sq.m. BUA</strong><br><br>
          2. Existing Consumed Heritage Built-Up Area:<br>
          &nbsp;&nbsp;&bull; Consumed In-Situ Heritage BUA = <strong>600 sq.m.</strong><br><br>
          3. Deprived Development Potential (Reg 14.5.5):<br>
          &nbsp;&nbsp;&bull; Unconsumed BUA Deprived by Covenants = 2,400 - 600 = <strong>1,800 sq.m.</strong><br><br>
          4. Heritage DRC Entitlement:<br>
          &nbsp;&nbsp;&bull; Heritage TDR Granted = 1,800 sq.m. BUA<br>
          &nbsp;&nbsp;&bull; Development Right Certificate (DRC) issued in square meters with generating plot coordinates.<br><br>
          5. Monetization &amp; Maintenance Tie-in (Reg 14.5.4):<br>
          &nbsp;&nbsp;&bull; DRC can be sold on the open market for consumption on receiving plots across developable zones.<br>
          &nbsp;&nbsp;&bull; Proceeds provide capital liquidity to the trust to maintain the existing 600 sq.m. haveli in an ideal state of preservation.
        </div>
        <p style="font-size:0.85rem; color:var(--ink-soft); margin:0;">
          <strong>Legal Scrutiny:</strong> The DRC will be issued only after the owner executes a registered undertaking agreeing to maintain the heritage structure in perpetuity without demolition or unauthorized alterations.
        </p>
      </div>
    """,
    'pitfalls_html': """
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 1: Undertaking Repairs Without HCC Prior Written Permission</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Under Reg 14.5.3, even routine maintenance like external repainting, replastering, or replacing wooden railings requires prior written permission in consultation with the HCC. Executing unauthorized modern cladding can trigger criminal penalties and forfeiture of development rights.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 2: Delegating the Power to Overrule the HCC</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          The proviso to Reg 14.5.3 strictly mandates that the power to overrule the HCC's advice rests exclusively with the Municipal Commissioner / Collector and <em>"shall not be delegated to any other officer."</em> Orders passed by Deputy Commissioners overruling HCC are ultra vires and invalid.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 3: Erecting Commercial Billboards on Heritage Facades</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Regulation 14.5.9 strictly prohibits outdoor display structures and advertising hoardings on heritage structures. Billboard rental contracts signed by heritage building owners are null and void under the UDCPR.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <p style="font-size:0.9rem; line-height:1.6; margin:0 0 10px 0;">
        <strong>Statutory Preservation Continuity:</strong> Regulation 14.5.2 explicitly upholds all heritage lists approved prior to UDCPR-2020 enactment, 
        confirming their statutory validity without requiring fresh town planning notifications under Section 37 or 20 of the MRTP Act.<br>
        <strong>Appendix-L Standard:</strong> Mandated standardized documentation cards ensuring uniform criteria across all Municipal Corporations and Regional Plans in Maharashtra.
      </p>
    """,
    'quiz': [
        {
            'question': 'Which grade of heritage asset allows strictly NO interventions except essential structural strengthening using like-to-like materials?',
            'options': [
                'Grade - I',
                'Grade - II (A)',
                'Grade - II (B)',
                'Grade - III'
            ],
            'answer': 0,
            'explanation': 'Under Regulation 14.5.8, Heritage Grade - I mandates careful preservation where no interventions are permitted either on exterior or interior unless necessary for strengthening with like-to-like material.'
        },
        {
            'question': 'Who has the statutory authority to overrule the advice of the Heritage Conservation Committee (HCC)?',
            'options': [
                'Any Assistant Municipal Commissioner',
                'The Town Planning Officer in-charge',
                'The Municipal Commissioner / Collector in exceptional cases with recorded reasons (non-delegable)',
                'The State Tourism Development Officer'
            ],
            'answer': 2,
            'explanation': 'Regulation 14.5.3 mandates that only the Authority (Commissioner/Collector) may overrule HCC in exceptional cases with written reasons, and this power cannot be delegated.'
        },
        {
            'question': 'How is an owner compensated when heritage conservation covenants deprive them of using permissible in-situ FSI?',
            'options': [
                'Cash grant from the state treasury',
                'Exemption from property tax for 50 years',
                'Grant of Transferable Development Rights (Heritage TDR / DRC)',
                'Additional land allocation in an industrial park'
            ],
            'answer': 2,
            'explanation': 'Regulation 14.5.5 states that if the owner is deprived of using permissible FSI due to heritage covenants, he shall be compensated by grant of Heritage TDR.'
        },
        {
            'question': 'Are commercial advertising billboards permitted on listed heritage buildings under Regulation 14.5.9?',
            'options': [
                'Yes, on payment of 50% extra premium',
                'Yes, if illuminated with LED lighting',
                'Strictly prohibited on buildings of heritage and historic importance',
                'Permitted on Grade-III buildings only'
            ],
            'answer': 2,
            'explanation': 'Regulation 14.5.9 strictly prohibits outdoor display structures and advertising signs on buildings of architectural, aesthetic, or heritage importance.'
        }
    ]
}

if __name__ == '__main__':
    create_lesson_page(lesson_data)
